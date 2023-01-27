import urllib
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data_url = input('Enter URL:')
count = int(input('Enter count: '))
rpos = int(input('Enter position: '))

print('Retrieving: ',data_url)
for i in range(0, count):
    html = urllib.request.urlopen(data_url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    data_url = tags[rpos - 1].get('href')

result = tags[rpos - 1].contens[0]

print(result)