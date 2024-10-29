import requests      # requests library can get data from online websites
from bs4 import BeautifulSoup    # it prints the output in understandable format 

url = 'https://reddit.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract title of the page
page_title = soup.title.string
print(f"Page Title: {page_title}")

# Extract specific data (e.g., all links on the page)
all_links = soup.find_all('img')
for link in all_links:
    print(link.get('src'))