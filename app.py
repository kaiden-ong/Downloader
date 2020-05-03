# make sure you pip install wget
# and beautifulsoup (maybe beautifulsoup4)

import wget
from bs4 import BeautifulSoup

wget.download("http://www.wallace.ccfaculty.org/book/book.html", "book.html")
with open("book.html", "r") as file:
    data = file.read() 
print(data)

soup = BeautifulSoup(data, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
    href = link.get('href')
    
    # does href start with "http://"?
    if (href.startswith("http://")):
        continue

    url = "http://www.wallace.ccfaculty.org/book/" + href
    wget.download(url, href)