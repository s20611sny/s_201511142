
# coding: utf-8

# In[5]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://python.org/')

html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
nodes = sel(html)


# In[6]:

print len(nodes)
for i,node in enumerate(nodes):
    if i<20:
        print i, node.get('href'), node.text

