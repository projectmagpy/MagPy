import requests
from BeautifulSoup import BeautifulSoup

base_url = raw_input("Enter the url : ")
content = BeautifulSoup(requests.get(base_url).text)
print content