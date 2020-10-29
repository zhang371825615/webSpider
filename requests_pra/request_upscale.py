
import requests
import  requests.cookies
import json


print("含登陆信息的post请求")
"""登陆信息"""

url="http://uap.deppon.com/uap-logstatistics-service/systemGeneralize/menuAccessPathLog"
cookie="JSESSIONID=ZL0E5SE2XU84w9BEmHtQ0Ayp; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22198777%22%2C%22%24device_id%22%3A%221715713530078f-0c53e7bc04745c-3a61430c-921600-1715713530140%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221715713530078f-0c53e7bc04745c-3a61430c-921600-1715713530140%22%7D; Hm_lvt_55960cd84c8805514a154f17d8be6d68=1589959139,1590049494; TGC=eyJhbGciOiJIUzUxMiJ9.WlhsS2FHSkhZMmxQYVVwcllWaEphVXhEU214aWJVMXBUMmxLUWsxVVNUUlJNRXBFVEZWb1ZFMXFWVEpKYmpBdUxqSnpPR0ZIYTBadlRHSmFNMGxNWlVWSk5HZHROMUV1WlZwQ2FFdzVORjlPZUdVeFRtbFlhVmM1U1V0TGRHZEdZVWhrZDBwWE1GazNUa2t3ZVZvME1tMDJhRE13WlROd2JraGZUMGhmTjFKRVVrdGtiMnR0WW1sNE9YVjVaVnAxTnpOcGN6ZDVRemxGZFZoSllsSkVNazVvY1hsd05taExiMlJzWkVOdVNFZFViazVMU0daQlFXWmFiRE4yVVhwSWVtWmxVblJuVEZOTWRHMVBVWHBWTkdzd09URk9XR3RwTmxwUE5XRk1WMWR0UTBaMlMwbEVSamhFU1dOamJpMU9abVJKYW1aWWJrb3lhV3REZFRJeE5FeEVPVkpKV2tWNGVqRTVNek5RYzBaeVJ6RjBUMGxVVlc5b1pYcHNVMkYzVFVwR01FUm9RVWhtYTFKZk1rUlRZbVIxUkZobE4wbDZSMk5uYm5abmFIVlNiM0ZFYVdaMWNqWktkMlp2YlZkbFRVMTBkbGRhUmxwbFNIQmthVUV1TlhkS2RFUmphVUV3TW5sdGJWUmtRVTB5Vm1aSlVRPT0.itxwE-H-F7URJ1VSlpxFz7ipzFqJprY-kSHkxij9_VLpM0EY_fpR2uJVf8h701xCautAQfyDxeiSgmeEOk-NMA; U=aHR0cDovL3V1bXMuZGVwcG9uLmNvbS91dW1zLWNhcy1zZXJ2ZXIvbG9naW4; _TOKENUUMS=\"Si1GUExBQmdNWkFxaHRhd2pwVnhNMCtYLDE5ODc3NywxOTg3NzcsVzAwMDAwMTk3NTks6JCl6L+Q566h55CG56CU5Y+R6YOoLDE1OTA1NjQwNjU2ODA=\""


headers={
    #'cookie':cookie,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
}

#RequestsCookieJar构造Cookie
jar=requests.cookies.RequestsCookieJar()
cl=cookie.split(';')
for c in cl:
    key,value=c.split('=',1)
    jar.set(key,value)

data={'menuCode':'OMS_06002','menuName':'快递订单受理','accessPath':1,'systemName':'OMS'}

#res=requests.post(url,headers=headers,params=data,cookies=jar)
#print(res.text)



"""
Session

'Content-Type':'application/json;charset=UTF-8'请求提交
"""

s=requests.Session()
headers={
    'cookie':cookie,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Content-Type':'application/json;charset=UTF-8'
}
data={'password':'123@@','userName':'123'}
r1=s.post("http://at.deppon.com/api/user/login",data=json.dumps(data),headers=headers)
for a in r1.cookies.iteritems():
    print(a[0],'===',a[1])
r=s.get("http://at.deppon.com/#/questionTaskSearch")
print(r.text)


print(""".....先登录在访问的案例.....""")


'1、登录'
s1=requests.Session()
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
}
data={"action":"login","method":"POST","data":{"userId":"ad","password":"123@@"}}


r12=s1.post("http://flow.deppon.com/api/base/",data=json.dumps(data),headers=headers)
for a in r12.cookies.iteritems():
    print(a[0],'===',a[1])

'2.访问授权接口'
data={"action":"filter","method":"GET","data":{"id":"filter_type_partin_hi"}}
r=s1.post("http://flow.deppon.com/api/flow/",data=json.dumps(data),headers=headers)
print(r.text.encode('utf-8').decode('unicode_escape')) #转码问题








