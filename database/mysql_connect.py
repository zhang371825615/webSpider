import  pymysql
"""
db=pymysql.connect(host='localhost',user='root',password='btiz#!ard2Id',port=3306)
cursor=db.cursor()
cursor.execute('SELECT VERSION()')
data=cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()
"""

#创建表
"""db=pymysql.connect(host='localhost',user='root',password='btiz#!ard2Id',port=3306,db='spiders')
cursor=db.cursor()
d=cursor.execute("CREATE TABLE IF NOT EXISTS student(id varchar(255) primary  key,name  varchar(255) not null ,age int   not null)")
print(d)
cursor.close()

"""



#插入数据
"""
db=pymysql.connect(host='localhost',user='root',password='btiz#!ard2Id',port=3306,db='spiders')
cursor=db.cursor()
sql = 'INSERT INTO student(id, name, age) values(%s, %s, %s) '
params=['10001','zhangsan',13]
try:
    d=cursor.execute(sql,params)
    print(d)
    db.commit()
except  Exception as e:
    print(e)
    db.rollback()
finally:
    if db:
       db.close()

"""

#动态构造insert

def insert(tableName,dictParam):
    db = pymysql.connect(host='localhost', user='root', password='btiz#!ard2Id', port=3306, db='spiders')
    cursor = db.cursor()
    keys=','.join(dictParam.keys())
    values = ','.join(['%s']*len(dictParam))

    sql='INSERT INTO {table}({keys}) values({values})'.format(table=tableName,keys=keys,values=values)
    print(sql)
    try:
        t=tuple(dictParam.values())

        d = cursor.execute(sql,t)
        print(d)
        db.commit()
    except  Exception as e:
        print(e)
        db.rollback()
    finally:
        if db:
            db.close()


def update(tableName):
    pass




#insert('student',{'id':'10005','name':'lisi','age':22})



#mysql更新操作
"""
sql ='UPDATE student SET age = %s WHERE name = %s'
db = pymysql.connect(host='localhost', user='root', password='btiz#!ard2Id', port=3306, db='spiders')
cursor = db.cursor()
try:

    d = cursor.execute(sql, (99,'lisi'))
    print(d)
    db.commit()
except  Exception as e:
    print(e)
    db.rollback()
finally:
    if db:
        db.close()
"""


#删除condition is a tuple
def deleteConditionAND(tableName,condition):
    # condition: ex {"name='123'","age<12"}
    db = pymysql.connect(host='localhost', user='root', password='btiz#!ard2Id', port=3306, db='spiders')
    cursor = db.cursor()

    realcondition=' AND '.join(condition)
    sql = 'delete from {tableName}  where {condition}'.format(tableName=tableName,condition=realcondition)

    try:

        d = cursor.execute(sql)
        print(d)
        db.commit()
    except  Exception as e:
        print(e)
        db.rollback()
    finally:
        if db:
            db.close()


deleteConditionAND("student",{"age>1","name='lisi2'"})



def queryOne(tableName,condition):
    db = pymysql.connect(host='localhost', user='root', password='btiz#!ard2Id', port=3306, db='spiders')
    cursor = db.cursor()
    sql="select *  from  {tableName} where {condition}".format(tableName=tableName,condition=condition)
    data=None
    try:
        cursor.execute(sql)
        data= cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        db.close()
    return data


def queryAll(tableName,condition):
    db = pymysql.connect(host='localhost', user='root', password='btiz#!ard2Id', port=3306, db='spiders')
    cursor = db.cursor()
    sql="select *  from  {tableName} where {condition}".format(tableName=tableName,condition=condition)
    data=None
    try:
        cursor.execute(sql)
        data= cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        db.close()
    return data



print(queryOne('student',"name='lisi'"))
queryAll('student',"name='asd1'")
