from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://quotes.toscrape.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Locate quote elements
quote_elements = soup.find_all('div', class_='quote')

# Initialize a list to store extracted quotes
quotes_list = []

# Extract quotes from each quote element
for quote_element in quote_elements:
    # Find the quote text within the current quote element
    quote_text = quote_element.find(class_='text').get_text(strip=True)
    quotes_list.append(quote_text)

# Print the extracted quotes
for quote in quotes_list:
    print(f"Quote: {quote}")

# Store the extracted quotes in a DataFrame and Excel file
df = pd.DataFrame({'Quotes': quotes_list})
df.to_excel('quotes.xlsx', index=False)
