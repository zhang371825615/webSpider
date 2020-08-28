from urllib.robotparser import RobotFileParser
from urllib.request import urlopen


rp=RobotFileParser(url='https://www.baidu.com/robots.txt')

rp.read()

print(rp.can_fetch('*','https://www.baidu.com/'))


rp.set_url("https://www.jianshu.com/robots.txt")
rp.read()
print(rp.can_fetch('YisouSpider','https://www.jianshu.com/p/0d3c7ca67917'))
print(rp.can_fetch('*','https://www.ianshu.com/search?q=python&page=l&ty pe=collections'))



print('-----------------')
rp = RobotFileParser()
rp.parse(urlopen('https://www.zhihu.com/robots.txt').read().decode('utf-8').split('\n'))

print(rp.can_fetch('Googlebot', 'https://www.zhihu.com/question/264161961/answer/278828570'))
print(rp.can_fetch('*', 'https://www.zhihu.com/question/264161961/answer/278828570'))
