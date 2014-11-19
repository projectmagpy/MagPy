__author__ = 'T90'
__version__ = '1.0.0'

__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re
import urllib2
import HTMLParser


def searchhtml(keyword, num):
	moz = mechanize.Browser()
	moz.set_handle_robots(False)
	moz.addheaders = [('User-agent',
						  'Mozilla/5.0 (Windows NT 6.2; rv:33.0) Gecko/20100101 Firefox/33.0')]

	base_url = "https://search.yahoo.com/search?p="
	search_url = base_url + keyword.replace(' ', '+')

	htmltext = ""
	for i in range(0, num):
		htmltext += str(moz.open(search_url + "&b=" + str((i * 10) + 1)).read())

	return htmltext


def getlinks(keyword, num):
	results = []
	html = searchhtml(keyword, num)
	bs = BeautifulSoup(html).findAll('div', attrs={'class': 'res'})
	linkre = re.compile('<a.*href="([^"]*)".*>.*</a>')
	h3re = re.compile('<a[^>]*>(.*)</a>')
	for a in bs:
		item = str(BeautifulSoup(str(a)).find('h3'))
		heading = HTMLParser.HTMLParser().unescape(re.findall(h3re, item)[0].replace('<b>', '').replace('</b>', ''))
		turl = str(re.findall(linkre, item)[0]).split('/')
		for part in turl:
			if part.startswith('RU='):
				url = urllib2.unquote(str(part).split('=')[1])
		results.append([heading, url])
	return results


def display_results(keyword, num):
	results = getlinks(keyword, num)
	print "\nTop " + str(len(results)) + " results from Yahoo\n"
	for result in results:
		print result[0] + ", " + result[1]


if __name__ == '__main__':
	display_results("Google", 1)

