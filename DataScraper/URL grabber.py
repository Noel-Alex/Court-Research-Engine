import os
import urllib.request
import requests
import re
from bs4 import BeautifulSoup
import time
import json
import json
from bs4 import BeautifulSoup
import time


def extract_docfragment_links(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Regular expression to match the '/docfragment/<num>/' pattern
    docfragment_pattern = re.compile(r'/docfragment/\d+/')

    # List to store the matched URLs
    docfragment_links = []

    # Iterate through all 'a' tags in the HTML
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # Check if the href matches the pattern
        if docfragment_pattern.search(href):
            docfragment_links.append(href)

    return docfragment_links





"""
path_of_Supreme_court_json_file = "links_Supreme_Court.json"

f = open(path_of_Supreme_court_json_file, 'r+')
links_json = json.load(f)



links = {}
Links = []
links['supremecourt'] = Links
for i in range(1950, 2025):
    URL = base + f'/search/?formInput=doctypes:supremecourt fromdate:1-1-{i} todate: 31-12-{i}'
    Links.append(URL)

json_object = json.dumps(links, indent = 4)
with open("final_set.json", "w") as outfile:
    outfile.write(json_object)
"""


base = 'https://indiankanoon.org'
"""
path_of_Supreme_court_json_file = "final_set.json"
f = open(path_of_Supreme_court_json_file, 'r+')
links_json = json.load(f)"""

"""
pdfs = {}
for i in range(386000):
    print(i, end = ' ')
    URL = 'https://indiankanoon.org/search/?formInput=%20commercial%20court%20%20%20%20doctypes%3A%20judgments%20sortby%3A%20mostrecent' + f"&pagenum={i}"
    page = requests.get(URL)  # sending a request to the url
    soup = BeautifulSoup(page.content, 'html.parser')
    pdf_links = extract_docfragment_links(soup.prettify())
    if len(pdf_links) < 1:
        break

    else:
        pdfs[i] = [base+x for x in pdf_links]


json_object = json.dumps(pdfs, indent = 4)
with open("commercial court.json", "w") as outfile:
    outfile.write(json_object)




base = 'https://indiankanoon.org/'
year_links = [f"search/?formInput=doctypes:supremecourt fromdate:1-1-{i} todate: 31-12-{i}" for i in range(1950, 1960)]
pdfs = {}
for year in year_links:
    print(year)
    for page in range(100):
        print(page, end= ' ')
        URL = base +year +  f'&pagenum={page}'
        page = requests.get(URL)  # sending a request to the url
        soup = BeautifulSoup(page.content, 'html.parser')
        pdf_links = extract_docfragment_links(soup.prettify())
        if len(pdf_links) < 1:
            break

        else:
            pdfs[URL[52:64]+'-'+URL[78:83]+'-'+str(page)] = [base + x for x in pdf_links]

    print()"""




def url_grabber(start = 1950,end = 2025, save = None, force = False):
    base = 'https://indiankanoon.org/'

    if save is not None and os.path.exists(save):
        f = open(save, 'r+')
        links_json = json.load(f)
        start_year = max([int(i[13:17]) for i in links_json])
    else:
        f = open(save, 'w+')
        links_json = {}
        start_year = start

    if force:
        start_year = start

    year_links = [f"search/?formInput=doctypes:supremecourt fromdate:1-1-{i} todate: 31-12-{i}" for i in
                  range(start_year, end)]

    for year in year_links:
        print(year)
        for pages in range(100):
            print(pages, end=' ')
            URL = base + year + f'&pagenum={pages}'
            page = requests.get(URL)  # sending a request to the url
            soup = BeautifulSoup(page.content, 'html.parser')
            pdf_links = extract_docfragment_links(soup.prettify())
            if len(pdf_links) < 1:
                break

            else:
                links_json[URL[52:64] + '-' + URL[78:82] + '-' + str(pages)] = [base + x for x in pdf_links]

        print()

    json_object = json.dumps(links_json, indent=4)
    with open(save, "w") as outfile:
        outfile.write(json_object)

url_grabber(1990,end=2010, save= "supremecourt.json", force=True)
"""
URL = 'https://indiankanoon.org/doc/84936428/'
page = requests.get(URL) # sending a request to the url
soup = BeautifulSoup(page.content, 'html.parser')
text = soup.prettify()
print(text)

print(extract_docfragment_links(text))
"""

