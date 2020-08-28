import requests,json,xlwt

headers={

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Cookie':'User-Token=Bearer%20eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckstqwzAQRf9Fa29CHyHeFdpFoWmhPxDUaBwP2Bqhh2kp_fdao5GrZuVzpXsu2PhbhfSheqXNjFZ1Sqc4rvH97eXp9PB4fH7tNJ5mshjJo730E4Z4deRSGLuznsHrXhtT0cAEEWpiTzg5o_MN2QEvvaFKHgJNC3Rgz2Tycl7bguxtmRe3JJvjekj-i83KItY4oP2745EaZAPtQOUC7YJRRyTbZOBxQdmWJAPNt8nVJkr9-ns2WSac9npmu5CIJbBTUOoeHPnIfUERJLEh_F9JbiK9WjSV92KocuaiZhIxoONmfkoxI_cySC0F8NxjkCIzN5ma6snA-kZxM2puxHq0-fVAZhY0QDxQSNQSWCpY6uu_Dp9O9bu7w_1-f3tz2P38AgAA__8.zRdgE7SyKLs_TDJ3pot9PCHaPXccUBt0fqdzl_fedUpR89y8LhQmwuTZ20vDzkP1BIYkDd4ysgN6kBXc8jSe1Q; JSESSIONID=969F50E47F4F95BB87232D508269A8CB',
    'Accept':'application/json, text/plain, */*',
    'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckstqwzAQRf9Fa29CHyHeFdpFoWmhPxDUaBwP2Bqhh2kp_fdao5GrZuVzpXsu2PhbhfSheqXNjFZ1Sqc4rvH97eXp9PB4fH7tNJ5mshjJo730E4Z4deRSGLuznsHrXhtT0cAEEWpiTzg5o_MN2QEvvaFKHgJNC3Rgz2Tycl7bguxtmRe3JJvjekj-i83KItY4oP2745EaZAPtQOUC7YJRRyTbZOBxQdmWJAPNt8nVJkr9-ns2WSac9npmu5CIJbBTUOoeHPnIfUERJLEh_F9JbiK9WjSV92KocuaiZhIxoONmfkoxI_cySC0F8NxjkCIzN5ma6snA-kZxM2puxHq0-fVAZhY0QDxQSNQSWCpY6uu_Dp9O9bu7w_1-f3tz2P38AgAA__8.zRdgE7SyKLs_TDJ3pot9PCHaPXccUBt0fqdzl_fedUpR89y8LhQmwuTZ20vDzkP1BIYkDd4ysgN6kBXc8jSe1Q'
}


r=requests.get(url='http://117.78.60.39/api/shop/invitation/rule?departId=&sipDeviceId=&page=1&size=5000',headers=headers,)
print(r.text)

list=json.loads(r.text).get('data').get('list')
workbook = xlwt.Workbook(encoding='gbk')
sheet = workbook.add_sheet("order")
for index,it in enumerate(list):
       sheet.write(index, 0, it.get('departName'))
       sheet.write(index, 1, it.get('sipDeviceId'))
       sheet.write(index, 2, it.get('isDelete'))
       sheet.write(index, 3, it.get('endTime'))
       sheet.write(index, 4, it.get('startTime'))
       sheet.write(index, 5, it.get('id'))


workbook.save('order0807_2.xls')






