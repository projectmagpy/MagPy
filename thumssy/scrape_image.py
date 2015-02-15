import requests
from lxml import html
import sys
import urlparse, urllib

base_url = raw_input("Enter the url :")
response = requests.get(base_url)
parsed_body = html.fromstring(response.text)

images = parsed_body.xpath('//img/@src')
if not images:
    sys.exit("No images exists")

images = [urlparse.urljoin(response.url,url)for url in images]
print 'Found %s images' % len(images)
n = len(images)

for url in images:
    try:
        urllib.urlretrieve(url, 'images/%s' % url.split('/')[-1])
    except:
        print "error: " + url
    # r = requests.get(url)
    # f = open('images/%s' % url.split('/')[-1],'w')
    # f.write(r.content)
    # f.close()