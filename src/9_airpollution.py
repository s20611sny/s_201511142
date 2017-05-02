
# coding: utf-8

# In[13]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_open_gokr_ex.py', u'#!/usr/bin/env python\n# coding: utf-8\nimport os\nimport requests\nimport urlparse\nimport urllib\nimport mylib\n\n\ndef doIt():\n    # (1) service + operation\n    SERVICE=\'ArpltnInforInqireSvc\'\n    OPERATION_NAME=\'getMinuDustFrcstDspth\'\n    params1=SERVICE+"/"+OPERATION_NAME\n    # (2) query params encoding\n    _d=dict()\n    _d[\'dataTerm\']=\'month\'\n    params2 = urllib.urlencode(_d)\n    # (3) add my service key\n    keyPath=os.path.join(os.getcwd(), \'src\', \'key.properties\')\n    \n    key=mylib.getKey(keyPath)\n    keygokr=key[\'gokr\'] # keygokr=\'8Bx4C1%2B...\'\n    params=params1+\'?\'+\'serviceKey=\'+keygokr+\'&\'+params2\n    # (4) make a full url\n    _url=\'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc\'\n    url=urlparse.urljoin(_url,params)\n    # (5) get data\n    data=requests.get(url).text\n    print data[:300]\n\n\ndoIt()')


# In[14]:

get_ipython().system(u'python src/ds_open_gokr_ex.py')

