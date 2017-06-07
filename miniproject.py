import requests
import json

url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr
geojson=json.loads(geostr)
current_latitude=geojson['latitude']
current_longitude=geojson['longitude']

dataseoul=6f4f416a6f73323039384a6f677670



import os
import requests
import urlparse
import mylib
import json
def FineDust():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    KEY=key['finedust']
    TYPE='json'
    SERVICE='InfoEmrrmLc'
    START_INDEX=str(1)
    END_INDEX=str(10)
    params='/'+KEY+'/'+TYPE+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX
    _url='http://openapi.seoul.go.kr:8088/6f4f416a6f73323039384a6f677670/xml/InfoEmrrmLc/1/5/'
    url=urlparse.urljoin(_url,params)
    data=requests.get(url).text
    jd = json.loads(data)
    for item in jd['InfoEmrrmLc']['row']:
        for i in item.keys():
            if i=='WGS84_LO':
                longitude= item.values()[15]
            if i=='WGS84_LA':
                latitude=item.values()[16]

if __name__ == "__main__":
    FineDust()
