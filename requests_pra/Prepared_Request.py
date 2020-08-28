"""
封装成一个request对象进行请求
"""


from requests import Request, Session


headers={

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
    'Cookie':'User-Token=Bearer%20eyJhbGciOiJSUzI1NiIsInppcCI6IkRFRiJ9.eNpckt1KxDAQhd8l171wEX-2d4JeCKuCL1DiZro70GZCfooivrvNZFLjXvU7yfkOtPRbhfSheqXNjFZ1Sqd4XuP72-FpeHh8eX7tNA4zWYzk0Z76CUO8OHIpnLujnsHrXhtT0cAEEWpiTzg5o_MN2RFPvaFKHgJNC3Rgj2Tycl7bguxtmRe3JJvn9ZD8F5uVRaxxRPt3xyM1yAbakcoF2gWjjki2ycDjgrItSQaab5OrTZT65fdsskw47fXMdiERS2CnoNQ9OPKR-4IiSGJD-L-S3ER6tWgq78VQ5cxFzSRiQMfN_JRiRu5lkFoK4LnHIEVmbjI11cHA-kZxM2puxHq0-fVAZhY0QDxQSNQSWCpY6uu_Dp9O9bub_e3d1X53f_3zCwAA__8.YTV7wjqo4rUygLmmIAXquqc2HnDCw4fl8h6Wx8aL1qQZ3VHSWFzS4nU9o6FK8lr13XZJNxrzkUUGZcseQVKrwg; JSESSIONID=4AF391E24458A1F8D1DA7A6399562849'
}

data={'name':'zhangsan'}

url='http://117.78.60.39/api/shop/invitation/rule?departId=&sipDeviceId=&page=1&size=5000'

s1=Session()
r1=Request('POST',url=url,headers=headers,data=data)

pre=s1.prepare_request(r1)
r=s1.send(pre)
print(r.text)