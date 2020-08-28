

import  requests
import  urllib3
import  random
urllib3.disable_warnings()

try:
   res=requests.get('https://www.12306.cn',verify=False)
   res.encoding = 'utf-8'
   print(res.status_code)
  # print(res.text)
except requests.exceptions.ConnectionError as e:
    print(e)



"""代理"""
proxies=[{'http':'http://27.191.234.69:9999','https':'https://58.215.213.230:8080'},
         {'http':'http://182.18.13.149:53281','https':'https://163.125.159.251:8888'}]

r1=requests.get('https://www.taobao.com/',proxies=random.choice(proxies),verify=False)
print(r1.text)
