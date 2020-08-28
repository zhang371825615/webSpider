

import urllib.request as request
import urllib.parse as parse
"""
urllib使用
"""
#GET请求urlopen
res=request.urlopen('http://www.deppon.com')
print(type(res.status))
print(res.getheaders())
print(res.getheader('Content-Type'))
#print(res.read().decode('utf-8'))


#GET带参数请求urlopen
data = bytes(parse.urlencode({'word':'hello'}), encoding='utf-8')
print(parse.urlencode({'word':'hello'}))#word=hello
response= request.urlopen('http://httpbin.org/post',data=data)
#print(response.read().decode('utf-8'))



print('........................')
#GET带参数请求---Request封装
#Nlass urllib_pra. request. Request (ur1, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
req=request.Request('https://python.org')
response = request.urlopen(req)
#print(response.read().decode('utf-8'))


#POST带参数请求---Request封装(headers\data)
url1 = 'http://httpbin.org/post'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','Host':'httpbin.org'}
d={'name':'Germey'}
data= bytes(parse.urlencode(d),encoding='utf8')
print(data)
req1=request.Request(url=url1,data=data,headers=headers,method='POST')
req.add_header('zhangsan','lis1')
res=request.urlopen(req1)
print(res.read().decode('utf-8'))
