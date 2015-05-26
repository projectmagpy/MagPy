__author__ = 'T90'
__version__ = '1.0.0'

import urllib
import mechanize
from BeautifulSoup import BeautifulSoup
from urlparse import urlparse
import hashlib


def searchPic(term):
    img_list = getPic(term)
    if len(img_list) > 0:
        for img in img_list:
            savePic(img)
    print "done..."


def getPic(search):
    search = search.replace(" ", "%20")
    # try:
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User-agent', 'Mozilla')]

    htmltext = browser.open(
        "https://www.google.com/search?site=&tbm=isch&source=hp&biw=995&bih=775&gs_l=img.3..0l10.15017.15339.0.25312.4.4.0.0.0.0.146.290.0j2.2.0.msedr...0...1ac.1.64.img..2.2.290.3rpJmTHh5dU&q=" + search + "&oq=" + search)
    img_urls = []
    formatted_images = []
    soup = BeautifulSoup(htmltext)
    results = soup.findAll("a")
    for r in results:
        try:
            if "imgres?imgurl" in r['href']:
                print r
                img_urls.append(r['href'])
        except:
            a = 0
    for im in img_urls:
        print img_urls
        refer_url = urlparse(str(im))
        image_f = refer_url.query.split("&")[0].replace("imgurl=", "")
        formatted_images.append(image_f)

    return formatted_images

    # except:
    #     return []


def savePic(url):
    print url
    hs = hashlib.sha224(url).hexdigest()
    file_extension = url.split(".")[-1]
    uri = ""
    dest = uri + hs + "." + file_extension
    print dest
    try:
        urllib.urlretrieve(url, dest)
    except:
        print "save failed"


searchPic(raw_input("Enter keyword : "))
