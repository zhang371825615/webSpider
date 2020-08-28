import pymongo


client = pymongo . MongoClient(host='localhost',port=27017)
client = pymongo . MongoClient("mongodb://localhost:27017/")

db=client['test']
collection=db.students


student = {
'id':'20170101',
'name':'Jordan ',
'age ':20,
'gender':'male'}

studentList=[{
'id':'20170101',
'name':'Jordan ',
'age ':21,
'gender':'male'},{
'id':'20180101',
'name':'LUCY ',
'age ':22,
'gender':'male'},{
'id':'20110101',
'name':'Jordan ',
'age ':23,
'gender':'fmale'}]

collection.insert_many(studentList)


#查询批量
items=collection.find({'name':'LUCY '})
print(items)
for i in items:
    print(i)


item=collection.find_one({'name':'LUCY '})
print('find_one:',item)


