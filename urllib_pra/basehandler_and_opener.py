from urllib.request import  HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener,Request
from urllib.error import URLError
'''
网站授权案例urllib使用
'''
username ='zhangjiayi001'
password ='zjy001@@'
url='http://flow.deppon.com/login'

p=HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','Host':'httpbin.org'}
req=Request(url=url,headers=headers,method='GET')


try:
    res=opener.open(req)
    html=res.read().decode('utf-8')
    #print(html)
except URLError as e:
    print(e)



'''
网络爬虫使用代理案例
'''
from urllib.request import ProxyHandler

proxy_handler=ProxyHandler({'http':'http://220.196.42.158:8081','https':'https://221.226.20.158:8080'})
url1='http://www.baidu.com'
opener = build_opener(proxy_handler)
req=Request(url=url1,headers=headers,method='GET')
try:
    req = Request(url=url1, headers=headers, method='GET')
    #res=opener.open(req)
    #html=res.read().decode('utf-8')
    #print(html)
except URLError as e:
    print(e)




"""
Cookies 的处理就需要相关的 Handler 了 。
网络爬虫使用Cookies hanlder案例
"""

import http.cookiejar
from urllib.request import HTTPCookieProcessor
cookie=http.cookiejar.CookieJar()
handler =HTTPCookieProcessor(cookie)
opener =build_opener(handler)
#res=opener.open('http://www.baidu.com')
#for item in cookie:
 #print(item.name+'='+item.value)


"""网络爬虫使用Cookies 并且保存到文件"""
filename='cookies.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open('https://www.baidu.com/')
cookie.save(ignore_discard=True, ignore_expires=True)

"""保存在本地Cookies，读取加载"""
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(filename)
for item in cookie:
  print(item.name+'='+item.value)
