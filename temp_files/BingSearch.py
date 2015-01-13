__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re
import HTMLParser


def searchhtml(keyword, num):
	ie = mechanize.Browser()
	ie.set_handle_robots(False)
	ie.addheaders = [('User-agent',
					  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3) ')]

	base_url = 'http://www.bing.com/search?q='
	search_url = base_url + keyword.replace(' ', '+')

	htmltext = ""
	for i in range(0, num):
		htmltext += str(ie.open(search_url + "&first=" + str(i * 10)).read())

	return htmltext


def getlinks(keyword, num):
	results = []
	html = searchhtml(keyword, num)
	bs = BeautifulSoup(html).findAll('li', attrs={'class': 'b_algo'})
	linkre = re.compile('<a.*href="([^"]*)".*>.*</a>')
	h2re = re.compile('<a[^<>]*>(.*)</a>')
	for a in bs:
		item = str(BeautifulSoup(str(a)).find('h2'))
		heading = HTMLParser.HTMLParser().unescape(
			re.findall(h2re, item)[0].replace('<strong>', '').replace('</strong>', ''))
		results.append([heading, re.findall(linkre, item)[0]])
	return results


def display_results(keyword, num):
	results = getlinks(keyword, num)
	print "\nTop " + str(len(results)) + " results from Bing\n"
	for result in results:
		print result[0] + ", " + result[1]


if __name__ == '__main__':
	display_results("Google", 1)