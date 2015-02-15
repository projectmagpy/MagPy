import urllib2
import lxml.html
import urlparse
import sys

base_url = raw_input("Enter the url :")
#response = requests.get(base_url)
res = urllib2.urlopen(base_url)
tree = lxml.html.fromstring(res.read())

ns = {'re': 'http://exslt.org/regular-expressions'}
pdf_files = tree.xpath('//a[re:test(@href, "\.pdf$", "i")]', namespaces=ns)

if not pdf_files:
    sys.exit("No files exists")

for node in pdf_files:
    pdf_files = [urlparse.urljoin(base_url, node.attrib['href'])for url in pdf_files]

print 'Found %s files' % len(pdf_files)
print pdf_files




#for node in pdf_files:

#   print urlparse.urljoin(base_url, node.attrib['href'])
