__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re
import HTMLParser


def searchhtml(keyword, num):
	chrome = mechanize.Browser()
	chrome.set_handle_robots(False)
	chrome.addheaders = [('User-agent',
						  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]

	base_url = 'https://www.google.co.in/search?q='
	search_url = base_url + keyword.replace(' ', '+')

	htmltext = ""
	for i in range(0, num):
		htmltext += str(chrome.open(search_url + "&start=" + str(i * 10)).read())

	return htmltext


def getlinks(keyword, num):
	results = []
	html = searchhtml(keyword, num)
	bs = BeautifulSoup(html).findAll('li', attrs={'class': 'g'})
	linkre = re.compile('<a.*href="([^"]*)".*>.*</a>')
	h3re = re.compile('<a.*>(.*)</a>')
	for a in bs:
		item = str(BeautifulSoup(str(a)).find('h3'))
		heading = HTMLParser.HTMLParser().unescape(re.findall(h3re, item)[0])
		results.append([heading, re.findall(linkre, item)[0]])
	return results


def display_results(keyword, num):
	results = getlinks(keyword, num)
	print "\nTop " + str(len(results)) + " results from Google\n"
	for result in results:
		print result[0] + ", " + result[1]


if __name__ == '__main__':
	display_results("Hello World", 1)