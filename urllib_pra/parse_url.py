"""
解析链接
URL的标准处理

"""

from urllib.parse import urlparse,urlunparse,urlencode,parse_qs,parse_qsl


result=urlparse('http://www.baidu.com/index.html;user,23?id=S&ldf=123#comment')
print(type(result),result)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user,23', query='id=S&ldf=123', fragment='comment')
"""
ParseResult分为6个部分\
"""



data =['http','www.baidu.com ','index.html','Puser','a=6', 'comment']
print(urlunparse(data))


print(urlencode({'abc':123,'cde':'456'}))
print(parse_qs('ad=123&ad=他&b=sd'))#参数转化字典{'ad': ['123', '他'], 'b': ['sd']}
print(parse_qsl('ad=123&b=123&b=老师'))#参数转化元祖 [('ad', '123'), ('b', '123'), ('b', '老师')]
"""
 quote() 该方法可以将内容转化为 URL 编码的格式 。 URL 中带有中文参数时，有时可能会导致乱码的问
unquote
"""

