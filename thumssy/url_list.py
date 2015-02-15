import requests
from BeautifulSoup import BeautifulSoup

url_list = raw_input("Enter url list    :")
url = url_list.split(",")
for urls in url:
    print urls
    print BeautifulSoup(requests.get(urls).text)