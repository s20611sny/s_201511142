
# coding: utf-8

# In[1]:

import requests
r=requests.get('http://www.kbreport.com/main')


# In[2]:

import lxml.etree
_htmlTree = lxml.etree.HTML(r.text)


# In[3]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_crawl_kbaseball.py', u'# coding: utf-8\nimport requests\nimport lxml.etree\n\ndef getkb():\n    r = requests.get(\'http://www.kbreport.com/main\')\n    _htmlTree = lxml.etree.HTML(r.text)\n    nodes = _htmlTree.xpath("//div[@class=\'team-rank-box\']//table[@class=\'team-rank\']//tr")\n    print u"\ud14c\uc774\ube14 \ud589 \uac2f\uc218: ", len(nodes)\n    counter=0\n    for teams in nodes:\n        for cols in teams:\n            if cols.xpath(\'.//a/text()\'):\n                print cols.xpath(\'.//a/text()\')[0],\n            else:\n                print cols.text.strip(),\n        print\n\ndef main():\n    getkb()\n\nif __name__ == "__main__":\n    main()')

