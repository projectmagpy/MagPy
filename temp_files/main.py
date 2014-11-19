from Scrapping_Experiments.Search import YahooSearch as yahoo, GoogleSearch, BingSearch

__author__ = 'T90'
__version__ = '1.0.0'

from threading import Thread

if __name__ == '__main__':
	"""
	This program is designed to print the title and links of the top results corresponding to the search keyword,
	separately from Google, Yahoo and Bing.

	keyword : the word to be searched
	num : How many pages of Google, Yahoo and Bing needs to be searched. The larger the value, the larger the number of
			results, and also larger the time and network usage

	"""
	keyword = raw_input("Enter the search key : ")
	num = input("How many pages should I search? ")
	gTH = Thread(target=goog.display_results, args=(keyword, num))
	bTH = Thread(target=bing.display_results, args=(keyword, num))
	yTH = Thread(target=yahoo.display_results, args=(keyword, num))

	Th = [gTH, bTH, yTH]

	for t in Th:
		t.run()

	for t in Th:
		t.join()
