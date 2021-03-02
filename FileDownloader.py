#!/usr/bin/env Python

import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#define the user agent browsers, so we can actually access the page
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple WebKit/537.36 (KHTML, like Gecko) Chrome970.0.3538.77 Safari/537.36"
}

Url = "https://www.stoningtonschools.org/board-of-ed/past-agendas"
folder_location = 'C:\\Users\\Ben\\Desktop\\SPS\\FileDownloader\\files\\'

#undesireable links
filters = ["view", "watch?", "projector=", "obj="]

#if not os.path.exists(folder_location):os.mkdir(folder_location)

def getLinks(URL):
    response = requests.get(URL, headers=headers, timeout=5)
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')

    # get main content of page, so we don't parse through navigation and footer links
    mainContent = soup.find('main')
    #findAll('a', attrs={'href': re.compile("^https?://")}):
    for link in mainContent.select("a[href]"):
        filename = os.path.join(folder_location, link['href'].split('/')[-1])

        if any (x in filename for x in filters):
            pass

        else:
            print ("Downloading: " + filename)
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(Url,link['href']), allow_redirects = True).content)


def main():
    getLinks(Url)


if __name__ == '__main__':
    main()
