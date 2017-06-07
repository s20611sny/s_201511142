
# coding: utf-8

# In[104]:

import requests 
import json 
 
 
url='http://freegeoip.net/json/' 
geostr=requests.get(url).text 
print geostr 
geojson=json.loads(geostr) 
current_latitude=geojson['latitude'] 
current_longitude=geojson['longitude'] 


# In[112]:

get_ipython().run_cell_magic(u'writefile', u'key.properties', u'dataseoul=6f4f416a6f73323039384a6f677670')


# In[115]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[116]:

import os
import requests
import urlparse
import json
keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)
KEY=key['dataseoul']
TYPE='json'
SERVICE='InfoEmrrmLc'
START_INDEX=str(1)
END_INDEX=str(100)
params='/'+KEY+'/'+TYPE+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX
_url='http://openapi.seoul.go.kr:8088/6f4f416a6f73323039384a6f677670/xml/InfoEmrrmLc/1/5/'
url=urlparse.urljoin(_url,params)
data=requests.get(url).text
jd = json.loads(data)

longitude_list=list()
latitude_list=list()
name_list=list()

for item in jd['InfoEmrrmLc']['row']:
    for i in item.keys():
        if i=='WGS84_LO':
            longitude_list.append(item.values()[15])
        elif(i=='WGS84_LA'):
            latitude_list.append(item.values()[1])
        elif(i=='INSTT_NM'):
            name_list.append(item.values()[0])   

for x in range(0,len(longitude_list)):
    if ((abs(current_longitude-longitude_list[x])<0.05) and (abs(current_latitude-latitude_list[x])<0.05)):
        print name_list[x]

