#!/usr/bin/env Python

import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#define the user agent browsers, so we can actually access the page
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple WebKit/537.36 (KHTML, like Gecko) Chrome970.0.3538.77 Safari/537.36"
}

def getLinks(URL):
	response = requests.get(URL, headers=headers, timeout=5)
	page = response.text
	soup = BeautifulSoup(page, 'html.parser')

	# get main content of page, so we don't parse through navigation and footer links
	mainContent= soup.find('main')

	for link in mainContent.findAll('a', attrs={'href': re.compile("^https?://")}):


def main():
	URL = "https://www.stoningtonschools.org/board-of-ed/meeting-minutes"


if __name__ == '__main__':
	main()