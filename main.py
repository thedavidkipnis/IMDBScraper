# DAVID KIPNIS
# 02-28-2023
# Simple webscraping program to gather list of most popular IMDB movies for a year

import urllib3
from bs4 import BeautifulSoup


def scrape(year: int):
    url = "http://www.imdb.com/search/title?release_date=" + str(year) + "," + str(year) + "&title_type=feature"

    x = urllib3.PoolManager().request('GET', url).data
    soup = BeautifulSoup(x, 'html.parser')

    movies = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})

    for m in movies:
        div = m.find('div', attrs={'class': 'lister-item-content'})
        header = div.findChildren('h3', attrs={'class': 'lister-item-header'})
        t = str(header[0].findChildren('a')[0].contents[0])
        print(t)


if __name__ == "__main__":
    year_in = None
    while year_in is None:
        try:
            yn = int(input("Which year would you like to know about? > "))
            if 2022 >= yn > 1900:
                year_in = yn
            else:
                print("Please enter a valid year [1900 - 2022]")
        except ValueError:
            print("Please enter a valid year [1900 - 2022]")

    scrape(year_in)
