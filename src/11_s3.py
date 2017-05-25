
# coding: utf-8

# In[ ]:

import os
import sys 
os.environ["SPARK_HOME"]="D:\\Code\\201511142\\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))


# In[7]:

import pyspark
myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder.master("local").appName("myApp").config(conf=myConf).config('spark.sql.warehouse.dir','file:///D:/Code/201511142/data').getOrCreate()


# In[6]:

myRdd2=spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki.txt"))
print myRdd2.first()


# In[1]:

import os
lines=spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki.txt"))
wc=lines.flatMap(lambda x: x.split(' '))
print type(wc)
print wc.collect()[:]
print "---> 한글로 출력:",wc.collect()[10]


# In[2]:

from operator import add
wc = spark.sparkContext.textFile(os.path.join("data","ds_spark_wiki.txt")).flatMap(lambda x: x.split(' ')).map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1)).reduceByKey(add)
print wc.count()
print wc.first()


# In[3]:

from operator import add
wc = spark.sparkContext.textFile("data/ds_spark_wiki.txt").map(lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower()).map(lambda x:x.split()).map(lambda x:[(i,1) for i in x])
for e in wc.collect():
    print e


# In[ ]:

get_ipython().system(u'D:/Code/201511142/spark-2.0.0-bin-hadoop2.6/bin/spark-submit')

