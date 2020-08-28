"""\
JSON存儲文件
"""

import json
str='''[{"name":"bob","age":12},
        {"name":"zjb","age":91}]'''

json.loads(str)




with open("data.json",'r') as a:
     str=a.read()
     jsonData=json.loads(str)
     print(jsonData[0])