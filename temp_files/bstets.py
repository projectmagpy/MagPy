from BeautifulSoup import BeautifulSoup as bs
import urllib

b = bs(urllib.urlopen("http://www.crummy.com/software/BeautifulSoup/bs3/documentation.html").read())

t = b.findParent(text="Modifying the Parse Tree")
print b.findPrevious(text="Modifying the Parse Tree")
print t

x = [tag for tag in b.find(text="Modifying the Parse Tree").findParents()]

id = x[0].id
i = 0
while id is None and i < len(x):
	id = x[i].id
	print x[i].name, x[i].id, x[i].class_
	i += 1