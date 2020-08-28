import  requests,json,xlwt,xlrd

headers={

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
  #  'Cookie':'User-Token=Bearer%20eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckstqwzAQRf9Fa2-yCE28K7SLQh_QHzBqNI4HbI3Qw7SU_nut0chVs_K50j0XbPytQvpQvdJmQas6pVOctvj-9vw43D-8PL12GoeFLEbyaK_9jCHeHLkUpu6iF_C618ZUNDBDhJrYE07O6HxDdsRrb6iSh0DzCh3YC5m8nNf2IHt75sU9yea0HZL_YrOyiDWOaP_ueKQG2UA7UrlAu2LUEck2GXhcULYlyUDzbXK1iVK__Z5NlgmnvV7YLiRiCewUlLoHRz5yX1AESWwI_1eSm0lvFs3lvRiqnLmomUQM6LiZn1LMyL0MUksBPPcYpMjMTaamOhjY3ijuRs2NWI92vx7IzIoGiAcKiVoCSwVLffvX4dOp_nA83x0O5-Pp9PMLAAD__w.sjc4W40BcYybZX6G6PLJXQg8LOquUbIQUa5DF3YHrmYDuDz9d0Vn8LVVwa9jvBeet1JLKkziPlGfq_TG6XAx2g; JSESSIONID=BDDEDE6CF9C1979C7E034BB2AAE1E69C',
    'Content-Type':'application/json;charset=UTF-8'
   # 'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckstqwzAQRf9Fa2-yCE28K7SLQh_QHzBqNI4HbI3Qw7SU_nut0chVs_K50j0XbPytQvpQvdJmQas6pVOctvj-9vw43D-8PL12GoeFLEbyaK_9jCHeHLkUpu6iF_C618ZUNDBDhJrYE07O6HxDdsRrb6iSh0DzCh3YC5m8nNf2IHt75sU9yea0HZL_YrOyiDWOaP_ueKQG2UA7UrlAu2LUEck2GXhcULYlyUDzbXK1iVK__Z5NlgmnvV7YLiRiCewUlLoHRz5yX1AESWwI_1eSm0lvFs3lvRiqnLmomUQM6LiZn1LMyL0MUksBPPcYpMjMTaamOhjY3ijuRs2NWI92vx7IzIoGiAcKiVoCSwVLffvX4dOp_nA83x0O5-Pp9PMLAAD__w.sjc4W40BcYybZX6G6PLJXQg8LOquUbIQUa5DF3YHrmYDuDz9d0Vn8LVVwa9jvBeet1JLKkziPlGfq_TG6XAx2g'
}


#1、登陆
s=requests.Session()
#登陆
data={"username":"admin","password":"admin456"}
r1=s.post("http://117.78.60.39/api/user/login",data=json.dumps(data),headers=headers)
print(r1.text)
#2、设置登陆授权
headers['Authorization']=json.loads(r1.text).get('data')
#3、发起请求
url='http://117.78.60.39/api/sip/info/findSipInfo?page=1&size=17000'
data={"sipDeviceId":"","departTypeCode":"","sipType":"","sipStatus":""}
data=json.dumps(data)
r1=requests.post(url=url,data=data,headers=headers)


list=json.loads(r1.text).get('data').get('list')

workbook = xlwt.Workbook(encoding='gbk')
sheet = workbook.add_sheet("longtian_SIP")

for index,item in enumerate(list):
    sheet.write(index, 0, item.get('sipStatus'))
    sheet.write(index, 1, item.get('sipDeviceId'))
    sheet.write(index, 2, item.get('sipDeviceId')[12:])

    print(item)


workbook.save('longtian_SIP.xls')

