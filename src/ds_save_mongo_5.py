
# coding: utf-8

# In[ ]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_save_mongo_5.js', u'use myDB\nshow dbs\nshow tables\ndb.myCol.insert({"Persons":[{"id":"405", "\uc774\ub984":"js1"},{"id":"406", "\uc774\ub984":"js2"}]})\ndb.myCol.find({"Persons.\uc774\ub984":"js1"})')

