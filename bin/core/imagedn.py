import mechanize
from BeautifulSoup import BeautifulSoup
import constants
import os
import urllib


def download(search):
    search = search.replace(" ", "+")
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla')]
    url = "https://www.bing.com/?go=Submit&qs=n&form=QBLH&scope=images&sc=8-4&sp=-1&sk=&cvid=39dd92166bd44736b7ef0bc895eba8d5&q=" + search + "&pq=" + search
    html = br.open(url)
    bs = BeautifulSoup(html)
    files = []
    for i in bs.findAll("div", attrs={"class": "dg_u"}):
        files.append(i.find("img")['src2'])
    for i in bs.findAll("div", attrs={"class": "dg_b"}):
        files.append(i.find("img")['src2'])

    dir = constants.fileloc + "" + search.replace("+", "_") + '/'
    try:
        os.mkdir(dir)
    except:
        pass
    n = 0
    tot = len(files)
    for i in files:
        urllib.urlretrieve(i.split("&")[0], dir + str(n) + ".jpg")
        n += 1
        yield (n*100)/tot


