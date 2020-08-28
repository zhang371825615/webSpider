"""

 requests基本用法



"""

import requests


r=requests.get('https://www.baidu.com',params={'a':1})
print(type(r))
print(r.text)
print(r.encoding)


headers={

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Cookie':'User-Token=Bearer%20eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckt1KxDAQhd8l171wEX-2d4JeCKuCL1DiZro70GZCfooivrvNZFLjXvU7yfkOtPRbhfSheqXNjFZ1Sqd4XuP72-FpeHh8eX7tNA4zWYzk0Z76CUO8OHIpnLujnsHrXhtT0cAEEWpiTzg5o_MN2RFPvaFKHgJNC3Rgj2Tycl7bguxtmRe3JJvn9ZD8F5uVRaxxRPt3xyM1yAbakcoF2gWjjki2ycDjgrItSQaab5OrTZT65fdsskw47fXMdiERS2CnoNQ9OPKR-4IiSGJD-L-S3ER6tWgq78VQ5cxFzSRiQMfN_JRiRu5lkFoK4LnHIEVmbjI11cHA-kZxM2puxHq0-fVAZhY0QDxQSNQSWCpY6uu_Dp9O9bub_e3d1X53f_3zCwAA__8.YTV7wjqo4rUygLmmIAXquqc2HnDCw4fl8h6Wx8aL1qQZ3VHSWFzS4nU9o6FK8lr13XZJNxrzkUUGZcseQVKrwg; JSESSIONID=4AF391E24458A1F8D1DA7A6399562849'
}

#带参数的get请求
r=requests.get(url='http://117.78.60.39/api/shop/invitation/rule?departId=&sipDeviceId=&page=1&size=5000',headers=headers)
print(r.text)
print(r.json())#直接把返回值转化为json









headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
         'upgrade-insecure-requests':'1'}

r=requests.get(url='https://www.zhihu.com/explore',headers=headers)
print(r.text)



"""
抓取二进制数据
"""
print('-------------------')
r=requests.get("https://github.com/favicon.ico")
print(r.text)
print(r.content)
print(type(r.cookies))

for a in r.cookies.iteritems():
    print(a[0],'===',a[1])

with open('favicon.ico','wb') as f:
       f.write(r.content)




print('----------------------')

"""模拟文件上传"""


d1={'file':open('favicon.ico','rb')}

res=requests.post('http://httpbin.org/post',files=d1)
print(res.content)





