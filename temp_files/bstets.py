from BeautifulSoup import BeautifulSoup as bs
import urllib

b = bs(urllib.urlopen(
    "http://www.mapsofindia.com/railway-timetable/trivandrum-cntl-to-mangalore-cntl-route-of-maveli-express.html").read())
demo = ['ERNAKULAM JN', 'AMBALAPUZHA', 'KOZHIKODE']
t = []

for d in demo:
    t.append(b.find(text=d).previous)
print t

for i in xrange(0, len(t)):
    temp = []
    if t[i].get('id', None) is not None:
        print t[i].get('id')
    if t[i].get('class', None) is not None:
        print t[i].get('class')
    print t[i].name


