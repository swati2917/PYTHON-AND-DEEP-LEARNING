#import ...
#URL = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#r = requests.get(URL)
#print(r.content)

import urllib.request
from bs4 import BeautifulSoup
# import os UNUSED STATEMET


myLink = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
getLink=urllib.request.urlopen(myLink)
soup = BeautifulSoup(getLink,  "html.parser")
print(soup.h1.text)
for link in soup.findAll('a'):
    print(link.get('href'))
table = soup.find("table", { "class" : "wikitable sortable plainrowheaders" })

for row in table.findAll('tr'):
    for r in row.findAll('td'):
        #print(r)
        cells = r.text
        print(cells)

elements = row.find('th')
print(elements.text)