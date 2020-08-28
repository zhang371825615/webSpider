import  csv

#數組寫入方式
with open('data.csv','w',encoding='utf-8-sig',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['id','name','age'])
    writer.writerow(['10001','问ike',20])
    writer.writerow(['10002','问asd阿薩德1ik2e',18])


#dict的寫入方式
with open('data2.csv','w',encoding='utf-8-sig',newline='') as file:

    fieldnames = (['id','name','age'])
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{"id":1001,"name":"bob","age":12},{"name":"zj23b","age":21},{"name":"zjb","age":91}])



#讀取CSV

import pandas as pd
