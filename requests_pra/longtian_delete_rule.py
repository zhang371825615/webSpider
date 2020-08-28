import requests,json,xlwt,xlrd






headers={

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Cookie':'User-Token=Bearer%20eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckstqwzAQRf9Fa29CHyHeFdpFoWmhPxDUaBwP2Bqhh2kp_fdao5GrZuVzpXsu2PhbhfSheqXNjFZ1Sqc4rvH97eXp9PB4fH7tNJ5mshjJo730E4Z4deRSGLuznsHrXhtT0cAEEWpiTzg5o_MN2QEvvaFKHgJNC3Rgz2Tycl7bguxtmRe3JJvjekj-i83KItY4oP2745EaZAPtQOUC7YJRRyTbZOBxQdmWJAPNt8nVJkr9-ns2WSac9npmu5CIJbBTUOoeHPnIfUERJLEh_F9JbiK9WjSV92KocuaiZhIxoONmfkoxI_cySC0F8NxjkCIzN5ma6snA-kZxM2puxHq0-fVAZhY0QDxQSNQSWCpY6uu_Dp9O9bu7w_1-f3tz2P38AgAA__8.zRdgE7SyKLs_TDJ3pot9PCHaPXccUBt0fqdzl_fedUpR89y8LhQmwuTZ20vDzkP1BIYkDd4ysgN6kBXc8jSe1Q; JSESSIONID=969F50E47F4F95BB87232D508269A8CB',
    'Accept':'application/json, text/plain, */*',
    'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckstqwzAQRf9Fa29CHyHeFdpFoWmhPxDUaBwP2Bqhh2kp_fdao5GrZuVzpXsu2PhbhfSheqXNjFZ1Sqc4rvH97eXp9PB4fH7tNJ5mshjJo730E4Z4deRSGLuznsHrXhtT0cAEEWpiTzg5o_MN2QEvvaFKHgJNC3Rgz2Tycl7bguxtmRe3JJvjekj-i83KItY4oP2745EaZAPtQOUC7YJRRyTbZOBxQdmWJAPNt8nVJkr9-ns2WSac9npmu5CIJbBTUOoeHPnIfUERJLEh_F9JbiK9WjSV92KocuaiZhIxoONmfkoxI_cySC0F8NxjkCIzN5ma6snA-kZxM2puxHq0-fVAZhY0QDxQSNQSWCpY6uu_Dp9O9bu7w_1-f3tz2P38AgAA__8.zRdgE7SyKLs_TDJ3pot9PCHaPXccUBt0fqdzl_fedUpR89y8LhQmwuTZ20vDzkP1BIYkDd4ysgN6kBXc8jSe1Q'
}

data = xlrd.open_workbook('./order0807_1.xls')
sheet1 = data.sheet_by_name('order')
url='http://117.78.60.39/api/shop/invitation/rule/'
id=0
for i in range(sheet1.nrows - 1):
    if sheet1.cell(i, 0).value=='':
           id=int(sheet1.cell(i, 5).value)
           print(url + str(id))
           r = requests.delete(url=url + str(id), headers=headers, )
           print(r.text)


