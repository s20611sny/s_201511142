
# coding: utf-8

# In[192]:

get_ipython().run_cell_magic(u'writefile', u'src/key.properties', u'finedust=6a7a77597073323035357466574e77\nultrafinedust=4479436a557332303130306e65436452')


# In[193]:

get_ipython().run_cell_magic(u'writefile', u'src/mylib.py', u"def getKey(keyPath):\n    d=dict()\n    f=open(keyPath,'r')\n    for line in f.readlines():\n        row=line.split('=')\n        row0=row[0]\n        d[row0]=row[1].strip()\n    return d")


# In[194]:

get_ipython().run_cell_magic(u'writefile', u'src/__init__.py', u'import os')


# In[195]:

import sys
del sys.modules['src.mylib']


# In[197]:

get_ipython().run_cell_magic(u'writefile', u'src/open_dataseoul_finedust.py', u'import os\nimport requests\nimport urlparse\nimport mylib\nimport json\ndef doIt():\n    keyPath=os.path.join(os.getcwd(), \'src\', \'key.properties\')\n    key=mylib.getKey(keyPath)\n    KEY=key[\'finedust\']\n    TYPE=\'json\'\n    SERVICE=\'ForecastWarningMinuteParticleOfDustService\'\n    START_INDEX=str(1)\n    END_INDEX=str(10)\n    params=\'/\'+KEY+\'/\'+TYPE+\'/\'+SERVICE+\'/\'+START_INDEX+\'/\'+END_INDEX\n    _url=\'http://openAPI.seoul.go.kr:8088/6a7a77597073323035357466574e77/xml/ForecastWarningMinuteParticleOfDustService/1/1/\'\n    url=urlparse.urljoin(_url,params)\n    data=requests.get(url).text\n    jd = json.loads(data)\n    for item in jd[\'ForecastWarningMinuteParticleOfDustService\'][\'row\']:\n        for i in item.keys():\n            if i==\'ALARM_CNDT\':\n                print item.values()[4]\n\nif __name__ == "__main__":\n    doIt()')


# In[196]:

get_ipython().run_cell_magic(u'writefile', u'src/open_dataseoul_ultrafinedust.py', u'import os\nimport requests\nimport urlparse\nimport mylib\nimport json\n\ndef doIt():\n    keyPath=os.path.join(os.getcwd(), \'src\', \'key.properties\')\n    key=mylib.getKey(keyPath)\n    KEY=key[\'ultrafinedust\']\n    TYPE=\'json\'\n    SERVICE=\'ForecastWarningUltrafineParticleOfDustService\'\n    START_INDEX=str(1)\n    END_INDEX=str(10)\n    params=\'/\'+KEY+\'/\'+TYPE+\'/\'+SERVICE+\'/\'+START_INDEX+\'/\'+END_INDEX\n    _url=\'http://openAPI.seoul.go.kr:8088/4479436a557332303130306e65436452/xml/ForecastWarningMinuteParticleOfDustService/1/1/\'\n    url=urlparse.urljoin(_url,params)\n    data=requests.get(url).text\n    jd = json.loads(data)\n    for item in jd[\'ForecastWarningUltrafineParticleOfDustService\'][\'row\']:\n        for i in item.keys():\n            if i==\'ALARM_CNDT\':\n                print item.values()[4]\n    \n\nif __name__ == "__main__":\n    doIt()')

