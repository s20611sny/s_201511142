
# coding: utf-8

# In[2]:

import urllib
keyword='비오는'
f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
mydata = f.read();


# In[3]:

import re
p=re.compile('title=".*비.?오는.*"')
res=p.findall(mydata)
for item in res:
    print item


# In[6]:

import lxml.html
from lxml.cssselect import CSSSelector
html = lxml.html.fromstring(mydata)
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')
nodes=sel(html)
for node in nodes:
    print node.text_content()


# In[14]:

import lxml.html
from lxml.cssselect import CSSSelector

html = lxml.html.fromstring(mydata)
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')
nodes = sel(html)
for node in nodes:
    print node.text_content()


# In[15]:

from lxml.cssselect import CSSSelector
import lxml.html
import requests

keyword='비오는'
r = requests.get("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")

_html = lxml.html.fromstring(r.text)
sel = CSSSelector('table[summary] > tbody > ._tracklist_move > .name > a.title')
nodes = sel(_html)
for node in nodes:
    print node.text_content()


# In[16]:

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
for node in nodes:
    #print lxml.html.tostring(item)
    _name=_selName(node)
    _artist=_selArtist(node)
    _album=_selAlbum(node)
    if _name:
        print _artist[0].text_content().strip(),
        print "---",
        print _name[0].text_content(),
        print "---",
        print _album[0].text_content()

