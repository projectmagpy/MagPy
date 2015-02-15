from BeautifulSoup import BeautifulSoup as bs
import os
from urllib2 import urlopen
import urlparse
from urllib import urlretrieve

def take_url():
    url = raw_input("Enter the url :")
    soup = bs(urlopen(url))
    parsed = list(urlparse.urlparse(url))
    out_folder = "images/"

    for image in soup.findAll("img"):
        print "Image: %(src)s" % image
        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        outpath = os.path.join(out_folder, filename)
        try:
            if image["src"].lower().startswith("http"):
                urlretrieve(image["src"], outpath)
            else:
                urlretrieve(urlparse.urljoin(url, image["src"]), outpath)
        except:
            pass

if __name__ == "__main__":
    take_url()