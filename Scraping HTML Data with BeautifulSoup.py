import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_url = "http://py4e-data.dr-chuck.net/comments_1735227.html"
# Getting the html information and parsing it with BeautifulSoup
html = urllib.request.urlopen(data_url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# Getting a list with the "span" tags
tags = soup('span')

# Counting the sum of all the values within the span tags
count = 0
for tag in tags:
    # We need to cast them to int, as they're parsed as text strings
    count += int(tag.contents[0])

print(count)