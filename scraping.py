
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Load the Excel file containing URLs
file_path = r'C:\Users\Smile\web_scraping_assignment\Data.xlsx'
df = pd.read_excel(file_path, header=None)

# Extract URLs from the Excel file
urls = df[0].tolist()

# Function to scrape data from a URL
def scrape_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.text.strip() if soup.title else ''
        description = soup.find('meta', attrs={'name': 'description'})['content'].strip() if soup.find('meta', attrs={'name': 'description'}) else ''
        return {'URL': url, 'Title': title, 'Description': description}
    except Exception as e:
        return {'URL': url, 'Error': str(e)}

# Scrape data from each URL
scraped_data = [scrape_data(url) for url in urls]

# Convert the scraped data into a DataFrame
scraped_df = pd.DataFrame(scraped_data)

# Save the DataFrame to a CSV file
csv_file_path = 'scraped_data.csv' 
scraped_df.to_csv(csv_file_path, index=False)

print(f"Scraped data saved to {csv_file_path}")
