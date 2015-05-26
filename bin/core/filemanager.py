from BeautifulSoup import BeautifulSoup as bs
import os
from urllib2 import urlopen
import urlparse
from urllib import urlretrieve
import constants
import re


class filemanager():
    def __init__(self, url, format, direct=False):
        self.url = url
        self.format = format.split(",")
        self.direct = direct

    def manageimages(self):
        out_folder = constants.fileloc + "images/"
        try:
            os.mkdir(out_folder)
        except:
            pass

        if self.direct:
            urlretrieve(self.url, out_folder + "/" + self.url.split()[-2:])
        else:
            soup = bs(urlopen(self.url))
            parsed = list(urlparse.urlparse(self.url))
            totim = soup.findAll("img")
            tot = len(totim)
            n = 0
            for image in totim:
                n += 1
                filename = image["src"].split("/")[-1]
                parsed[2] = image["src"]
                outpath = os.path.join(out_folder, filename)
                try:
                    if image["src"].lower().startswith("http"):
                        urlretrieve(image["src"], outpath)
                    else:
                        urlretrieve(urlparse.urljoin(self.url, image["src"]), outpath)
                        yield (n*100)/tot
                except:
                    pass

    def managefiles(self):
        out_folder = constants.fileloc + "files/"
        try:
            os.mkdir(out_folder)
        except:
            pass

        if self.direct:
            urlretrieve(self.url, out_folder + "/" + self.url.split()[-2:])
        else:
            soup = bs(urlopen(self.url))
            parsed = list(urlparse.urlparse(self.url))
            tota = soup.findAll("a")
            tot = len(tota)
            n = 0
            for a in tota:
                n += 1
                filetype = a['href'].split(".")[-1]
                if filetype in self.format:
                    filename = a["href"].split("/")[-1]
                    parsed[2] = a["href"]
                    outpath = os.path.join(out_folder, filename)
                    try:
                        if a['href'].lower().startswith("http"):
                            urlretrieve(a['href'], outpath)
                        else:
                            urlretrieve(urlparse.urljoin(self.url, a['href']), outpath)
                            yield (n*100)/tot
                    except:
                        pass

    def manageregex(self, pattern):
        out_folder = constants.fileloc + "files/"
        try:
            os.mkdir(out_folder)
        except:
            pass

        if self.direct:
            urlretrieve(self.url, out_folder + "/" + self.url.split()[-2:])
        else:
            soup = bs(urlopen(self.url))
            parsed = list(urlparse.urlparse(self.url))
            tota = soup.findAll("a")
            tot = len(tota)
            n = 0
            pat = re.compile(pattern)
            for a in tota:
                n += 1
                try:
                    if pat.match(str(a['href'])):
                        filename = a["href"].split("/")[-1]
                        parsed[2] = a["href"]
                        outpath = os.path.join(out_folder, filename)
                        if a['href'].lower().startswith("http"):
                            urlretrieve(a['href'], outpath)
                        else:
                            urlretrieve(urlparse.urljoin(self.url, a['href']), outpath)
                            yield (n*100)/tot
                except:
                    pass


if __name__ == '__main__':
    for i in filemanager(url="http://en.wikipedia.org/wiki/Orange_(fruit)", direct=False, format='jpg, png').manageimages():
        print i