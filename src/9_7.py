
# coding: utf-8

# In[7]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_open_subwayPassengers.py', u'# coding: utf-8\nimport os\nimport requests\nimport json\nfrom pymongo import MongoClient\nimport mylib\n\nClient = MongoClient(\'localhost:27017\')\n_db=Client[\'ds_open_subwayPassengersDb\'] #db created by mongo\n_table=_db[\'db_open_subwayTable\'] #collection\n#db=Client.ds_rest_subwayPassengers\n\ndef saveJson(_fname,_data):\n    import io\n    with io.open(_fname, \'a\', encoding=\'utf8\') as json_file:\n        _j=json.dumps(_data, json_file, ensure_ascii=False, encoding=\'utf8\')\n        json_file.write(_j+"\\n")\n\ndef readJson(_fname):\n    for line in open(_fname, \'r\').readlines():\n        _j=json.loads(line)\n        #print _j[\'id\'],_j[\'text\']\n        print _j[\'id\']\n\ndef saveDB(_data):\n    _table.insert_one(_data)\n\ndef readDB():\n    for tweet in _table.find():\n        print tweet[\'id\'],tweet[\'text\']\n\ndef saveFile(_fname,_data):\n    fp=open(_fname,\'a\')\n    fp.write(_data+"\\n")\n\ndef doIt():\n    keyPath=os.path.join(os.getcwd(), \'src\', \'key.properties\')\n    key=mylib.getKey(keyPath)  \n    _key=key[\'dataseoul\'] #KEY=\'73725.....\'\n    _url=\'http://openAPI.seoul.go.kr:8088\'\n    _type=\'json\'\n    _service=\'CardSubwayStatisticsService\'\n    _start_index=1\n    _end_index=5\n    _use_mon=\'201306\'\n    _maxIter=20\n    _iter=0\n    _jfname=\'src/ds_open_subwayPassengers.json\'\n    while _iter<_maxIter:\n        _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)\n        #print _api\n        r=requests.get(_api)\n        _json=r.json()\n        print _json\n        saveJson(_jfname,_json)\n        saveDB(_json)\n        _start_index+=5\n        _end_index+=5\n        _iter+=1\n\nif __name__ == "__main__":\n    doIt()')


# In[8]:

get_ipython().system(u'python src/ds_open_subwayPassengers.py')


# In[9]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_open_subwayPassengers_mongo.js', u'use ds_open_subwayPassengersDb\ndb.db_open_subwayTable.find({"CardSubwayStatisticsService.row.SUB_STA_NM":"\uac15\ub0a8\uad6c\uccad"})')


# In[10]:

get_ipython().system(u'mongo < src/ds_open_subwayPassengers_mongo.js')

