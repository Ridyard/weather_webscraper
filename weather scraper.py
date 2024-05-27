
# simple script to scrape weather forecast in a given UK location

import webbrowser, sys, bs4, requests, random
from pathlib import Path


# simple scraping will be blocked by most sites - see this link for guidance to get around this: https://scrapeops.io/web-scraping-playbook/403-forbidden-error-web-scraping/
# this is a list of fake user agents, used to bypass anti-scraping functionality a site may have
# ie the website can't tell if the request is coming from a scraper or real user
# the called website will think one of the following devices is calling, intead of a py script
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

url = 'https://www.bbc.co.uk/weather/'
query = input("enter your post code to check the current weather...")
parts = query.split() 
query = parts[0] # keep the first half of the post code (eg m3, ec3m, ls1...)
res = requests.get(url + query, headers={'User-Agent': random.choice(user_agents_list)})
res.raise_for_status()

# parse html content
weatherContent = bs4.BeautifulSoup(res.text, 'html.parser')

# Find all <div> elements with the specific class attributes
containers = weatherContent.find_all('div', class_='ssrcss-10eqmzv-TextBlockContainer e18m38lv3')

# Initialize an empty list to hold the found <p> elements
elements = []

# Loop through each found container and search for the <p> elements within it
for container in containers:
    elements.extend(container.find_all('p', class_='ssrcss-1q0x1qg-Paragraph e1jhz7w10')) # .extend is similar to .append


# If you need a list of the element texts, you can extract them as follows
element_texts = [element.get_text() for element in elements]
for i in element_texts:
    print(i + '\n')


# webbrowser.open(url + query)
