import mechanize, HTMLParser, urllib2, urllib, requests
from BeautifulSoup import BeautifulSoup
import ranking_algo as alg


class basicnav():
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


class SearchEngine():
    """
    A Class designed to collect the links related to a certain keyword, passed as an argument to the constructor method
    of this class.
    The links are first collected from google, Yahoo and Bing, and is then used to retrieve the self.pages corresponding to
    these links, extract text from the links and return it.

    Class Managed By : Thumssy P. Nazar
    """

    def __init__(self, keyword, pages=1, type="text"):
        """
        The Constructor method.
        :param keyword: keyword to be searched
        :param type: Type of links to be collected (textual/image/video/file)
        :return: self.data
        """
        self.type = type
        self.keyword = keyword  # keyword to be searched
        self.pages = pages  # number of pages of search

        self.data = []  # the final data array. contains data as [[link, data], [link, data] ...]
        self.uniquelinks = []  # unique links collected from all search engines together


    def google_proc(self):
        chrome = mechanize.Browser()
        chrome.set_handle_robots(False)
        chrome.addheaders = [('User-agent',
                              'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]

        base_url = 'https://www.google.co.in/search?q='
        search_url = base_url + self.keyword.replace(' ', '+')

        htmltext = ""
        for i in range(0, self.pages):
            htmltext += str(chrome.open(search_url + "&start=" + str(i * 10)).read())
        self.glinks = self.google_formatter(htmltext)
        return self.glinks


    def bing_proc(self):
        ie = mechanize.Browser()
        ie.set_handle_robots(False)
        ie.addheaders = [('User-agent',
                          'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3) ')]

        base_url = 'http://www.bing.com/search?q='
        search_url = base_url + self.keyword.replace(' ', '+')

        htmltext = ""
        for i in range(0, self.pages):
            htmltext += str(ie.open(search_url + "&first=" + str(i * 10)).read())
        self.blinks = self.bing_formatter(htmltext)
        return self.blinks


    def yahoo_proc(self):
        moz = mechanize.Browser()
        moz.set_handle_robots(False)
        moz.addheaders = [('User-agent',
                           'Mozilla/5.0 (Windows NT 6.2; rv:33.0) Gecko/20100101 Firefox/33.0')]

        base_url = "https://search.yahoo.com/search?p="
        search_url = base_url + self.keyword.replace(' ', '+')

        htmltext = ""
        for i in range(0, self.pages):
            htmltext += str(moz.open(search_url + "&b=" + str((i * 10) + 1)).read())
        self.ylinks = self.yahoo_formatter(htmltext)
        return self.ylinks

    def google_formatter(self, data):
        """
        Format recieved links
        :param ddata:
        :return: formatted list
        """
        results = []
        bs = BeautifulSoup(data).findAll('div', attrs={'class': 'rc'})
        for a in bs:
            item = a.find('h3')
            heading = HTMLParser.HTMLParser().unescape(item.text)
            item = a.find('a')
            link = item['href']
            results.append(link)
        return results


    def yahoo_formatter(self, data):
        """
        Format recieved links
        :param ddata:
        :return: formatted list
        """
        results = []
        bs = BeautifulSoup(data).findAll('div', attrs={'class': 'compTitle'})
        for a in bs:
            item = a.find('h3')
            heading = HTMLParser.HTMLParser().unescape(item.text)
            turl = a.find('a')['href'].split("/")
            for part in turl:
                if part.startswith('RU='):
                    url = urllib2.unquote(str(part).split('=')[1])
            results.append(url)
        return results


    def bing_formatter(self, data):
        """
        Format recieved links
        :param ddata:
        :return: formatted list
        """
        results = []
        bs = BeautifulSoup(data).findAll('li', attrs={'class': 'b_algo'})
        for a in bs:
            item = a.find('h2')
            heading = HTMLParser.HTMLParser().unescape(item.text)
            item = a.find('a')
            link = item['href']
            results.append(link)
        return results


    def search(self, links=False):
        """
        Get links from the search engines and fill them to the respective lists.
        It gets self.pages of links from Search Engines, sends them to the formatter functions and gets the lists.
        :return: nothing
        """
        try:
            if self.type == "text":
                self.uniquelinks = alg.rank(self.google_proc(), self.yahoo_proc(), self.bing_proc())
                if links:
                    yield self.uniquelinks
                else:  # [[link, data], [link, data] ...]
                    for li in self.uniquelinks:
                        data, l = self.data_collector(li), len(self.uniquelinks)
                        yield [li, data, l]
        except:
            pass


    def data_collector(self, url):
        """
        Gets the HTML data from the page specified by the URL.
        :param url: url from which data is to be retrieved.
        :return: list with HTML data
        """
        try:
            html = urllib2.urlopen(url).read()
            return html
        except:
            pass


class recursivenav():
    def __init__(self, start, limit=200, possible_servers=""):
        self.starturl = start
        self.links = [self.starturl]
        self.visited = []
        self.limit = int(limit)
        self.servers = possible_servers.split(",")
        self.data = []

    def search(self, links=False):
        # if self.limit == 0:
        # self.limit = 100

        while len(self.links) > 0 and len(self.visited) < self.limit:
            l = self.links[0]
            htmlfile = urllib.urlopen(l)
            htmltext = htmlfile.read()
            print htmltext
            self.links.pop(0)
            self.visited.append(l)
            try:
                data = urllib.urlopen(l).read()
                self.data.append([l, data])
                bs = BeautifulSoup(data)
                for a in bs.findAll("a"):
                    if a['href'] != '':
                        if ".".join(self.starturl.split(".")[-2:]) in a['href']:
                            if "http://" not in a['href']:
                                link = urllib.basejoin(self.starturl, a['href'])

                                if link not in (self.links, self.visited):
                                    self.links.append(link)
                            else:
                                self.links.append(a['href'])

                if self.limit > -1:
                    self.limit -= 1
            except:
                pass
        if links:
            return self.visited
        else:
            return self.data


if __name__ == '__main__':
    for i in SearchEngine("hello world", pages=1).search(links=False):
        print i
    # print basicnav().listnav(["http://wikipedia.org", "http://www.marutisuzuki.com/swift.aspx"])
    # print recursivenav("http://www.thehindu.com").search()