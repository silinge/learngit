# I made this one as first day and see how far can T get.
# The code belong to the book's author.
#part one
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, features='lxml')
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])

#get href from this link