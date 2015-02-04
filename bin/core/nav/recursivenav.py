import urllib
from BeautifulSoup import BeautifulSoup


class recursivenav():
	def __init__(self, start, limit=0, possible_servers=[]):
		self.starturl = start
		self.links = [self.starturl]
		self.visited = []
		self.limit = limit
		self.servers = possible_servers
		self.data = []

	def search(self, links=False):
		while len(self.links) > 0 and self.limit>=len(self.visited):
			l = self.links[0]
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
	r = recursivenav("http://www.thehindu.com")
	x = r.search()
	for a in x:
		print a
	print len(x)