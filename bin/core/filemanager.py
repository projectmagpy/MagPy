from BeautifulSoup import BeautifulSoup as bs
import os
from urllib2 import urlopen
import urlparse
from urllib import urlretrieve


class FileManager():
    def __init__(self, url, type, limit, size, format, direct):
        self.url = url
        self.type = type
        self.limit = limit
        self.size = size
        self.format = format
        self.direct = direct
        if self.type == "img":
            self.manageimages()

    def DownloadImages(self):
        out_folder = "images/"

        if self.direct:
            urlretrieve(self.url, out_folder + "/" + self.url.split()[-2:])
        else:
            soup = bs(urlopen(self.url))
            parsed = list(urlparse.urlparse(self.url))
            for image in soup.findAll("img"):
                filename = image["src"].split("/")[-1]
                parsed[2] = image["src"]
                outpath = os.path.join(out_folder, filename)
                try:
                    if image["src"].lower().startswith("http"):
                        urlretrieve(image["src"], outpath)
                    else:
                        urlretrieve(urlparse.urljoin(self.url, image["src"]), outpath)
                except:
                    pass

    def DownloadFiles(self):
        out_folder = "files/"

        if self.direct:
            urlretrieve(self.url, out_folder + "/" + self.url.split()[-2:])
        else:
            soup = bs(urlopen(self.url))
            parsed = list(urlparse.urlparse(self.url))
            for a in soup.findAll("a"):
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
                    except:
                        pass


if __name__ == '__main__':
    fm = filemanager(url="http://en.wikipedia.org/wiki/Apple", type="img", size=-1, direct=False, format=['jpg', 'png'], limit=1)