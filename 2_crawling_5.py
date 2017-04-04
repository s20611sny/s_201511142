
# coding: utf-8

# In[2]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_crawl_ieee.py', u'# coding: utf-8\nimport lxml.html\nfrom lxml.cssselect import CSSSelector\nimport requests\nr = requests.get(\'http://www.ieee.org/conferences_events/conferences/search/index.html\')\n\nhtml = lxml.html.fromstring(r.text)\nsel=CSSSelector(\'div.content-r-full table.nogrid-nopad tr p>a[href]\')\nnodes = sel(html)\nfor node in nodes:\n    print node.text\n    print "----------"')

