import os
import requests
import urlparse
import mylib
import json

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    KEY=key['ultrafinedust']
    TYPE='json'
    SERVICE='ForecastWarningUltrafineParticleOfDustService'
    START_INDEX=str(1)
    END_INDEX=str(10)
    params='/'+KEY+'/'+TYPE+'/'+SERVICE+'/'+START_INDEX+'/'+END_INDEX
    _url='http://openAPI.seoul.go.kr:8088/4479436a557332303130306e65436452/xml/ForecastWarningMinuteParticleOfDustService/1/1/'
    url=urlparse.urljoin(_url,params)
    data=requests.get(url).text
    jd = json.loads(data)
    for item in jd['ForecastWarningUltrafineParticleOfDustService']['row']:
        for i in item.keys():
            if i=='ALARM_CNDT':
                print item.values()[4]
    

if __name__ == "__main__":
    doIt()