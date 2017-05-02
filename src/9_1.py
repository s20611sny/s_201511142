
# coding: utf-8

# In[11]:

import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr
type(geostr)


# In[14]:

import json
geojson=json.loads(geostr)
type(geojson)


# In[15]:

print geojson['ip']


# In[16]:

geojson.get('ip')


# In[18]:

country=geojson.get('country_code')
print country.decode('utf-8')


# In[ ]:

import json
import urllib

def getCountry(ipAddress):
    response = urllib.urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

print(getCountry("39.118.87.152"))


# In[20]:

import requests
send_url = 'http://freegeoip.net/json/39.118.87.152'
r = requests.get(send_url)


# In[19]:

j=json.loads(r.text)
type(j)


# In[21]:

print j.keys()
print j['city']


# In[22]:

for k,v in j.iteritems():
    print k,"\t: ",v

