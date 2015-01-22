import urllib
from BeautifulSoup import BeautifulSoup

starturl = "http://csebeta.x10.mx"
links = [starturl]
visited = []

while len(links) > 0:
    l = links[0]
    print len(l), l
    links.pop(0)
    visited.append(l)
    try:
        data = urllib.urlopen(l).read()
        bs = BeautifulSoup(data)
        for a in bs.findAll("a"):
            if a['href'] != '':
                if starturl in a['href']:
                    links.append(a['href'])
                elif "http://" not in a['href']:
                    link = urllib.basejoin(starturl, a['href'])
                    if link not in (links, visited):
                        links.append(link)
    except:
        print "err: " + l
