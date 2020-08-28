"""

URL Error 类来自 urllib_pra 库的 error 模块，它继承自 OS Error 类，是 error 异常模块的基类，
由 request捕模块生的异常都可以通过捕获这个类来处理。

"""

from urllib import request,error
"""
try:
    res=request.urlopen('http://www.deppon.com/index.html')
except error.URLError as e:
    print(e.reason)
"""
"""
它是 URL Error 的子类，专门用来处理 HTTP 请求错误，比如认证请求失败等 。 它有如下 3 个属性。
code\reason\headers
"""



try:
    res=request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
     print(e.reason)
     print(e.headers)