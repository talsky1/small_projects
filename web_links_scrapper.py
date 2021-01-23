import requests
import sys
from bs4 import BeautifulSoup

def extract(URL):
    
    print("Scanning -> " + URL)
    links = []
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        find_att = soup.find_all('a', href=True)   
        for a in find_att:
            if my_url in a['href']:
                links.append(a['href'])
    except:
        pass
    return list(set(links))

#user input:
try:
    URL = sys.argv[1]
except:
    print("!!!!! Wrong URL !!!!!!")
    URL = input("Please type your URL again: ")

my_url = URL.split("www")[1]
links = extract(URL)

links2 = []

for z in links:
    l = extract(z)
    links2 += l

links = links2 + links
links = list(set(links))

for x in links:
    print(x)