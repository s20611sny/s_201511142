
# coding: utf-8

# In[1]:

import urllib2
url = 'http://www.google.com/#q=python'
headers = {'User-Agent' : 'Mozilla 5.0'}
request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
print response.headers

