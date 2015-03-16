import requests

class nav():
    def single(self, url):
        return [url, requests.get(url).text]

    def listnav(self, urls):
        data = []
        for i in urls:
            print i
            temp = []
            temp.append([i, requests.get(i).text])
            data.append(temp)
        return data

    def iterativenav(self, url, type, start, stop):
        if type == "text":
            pass
        elif type == "num":
            data = []
            for i in xrange(start, stop + 1):
                nurl = url.replace("%d1", str(i))
                print nurl
                data.append([nurl, requests.get(nurl).text])
            return data


if __name__ == '__main__':
   print nav().listnav(["http://wikipedia.org","http://www.marutisuzuki.com/swift.aspx"])
  # print nav().iterativenav(url = "http://forum.xda-developers.com/showthread.php?t=779%d1",type = 'num',start = 100,stop = 103)