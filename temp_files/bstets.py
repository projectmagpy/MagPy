from BeautifulSoup import BeautifulSoup as bs
import urllib

b = bs(urllib.urlopen("http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html").read())

print [tag.name for tag in b.find(text="Modifying the Parse Tree").findParents()[0:3]]