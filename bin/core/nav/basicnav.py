import requests


class nav():
    def single(self, url):
        return [url, requests.get(url).text]

    def listnav(self, urls):
        data = []
        for i in urls:
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
                data.append([nurl, requests.get(nurl).text])
            return data


print nav().listnav(["http://wikipedia.org","http://www.marutisuzuki.com/swift.aspx"])