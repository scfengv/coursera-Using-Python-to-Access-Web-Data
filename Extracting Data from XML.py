# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1735229.xml (Sum ends with 6)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format and Approach
# The data consists of a number of names and comment counts in XML as follows:

# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

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