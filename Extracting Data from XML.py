import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

actual_data = "http://py4e-data.dr-chuck.net/comments_1735229.xml"

#We'll analyze this generic parameter, so we will only need to change its source
#and not every single one of its appearances in the code
#NOTE: I'm using Sublime Text and it doesn't accept raw_input, so I'll set the URL
#from here isntead from a user prompt
data_url = actual_data
data = urllib.request.urlopen(data_url, context=ctx).read()

#xml_data contains the commentinfo object, as it is the main structure, so we
#have to look for the comments element and then for all its comment elements
xml_data = ET.fromstring(data)
search_str = "comments/comment"
count_tags = xml_data.findall(search_str)

#Computing the sum
total_count = 0
for tag in count_tags:
	#We'll find the "count" element inside each "comment" element and add it
	count = tag.find('count')
	total_count += int(count.text)

print(total_count)