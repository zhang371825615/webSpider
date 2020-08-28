"""
pyquery
解析器
"""

from  pyquery import PyQuery as pq
import  requests

doc=pq(url='https://cuiqingcai.com')
print(doc('title'))


print(requests.get('https://cuiqingcai.com').text)
doc=pq(requests.get('https://cuiqingcai.com').content)
print(doc('title'))

#基本 css 选择器
text="""<div><ul id='ul1'><li class='item-0 active'>123<a href='www.baidu.com'>百度</a></li><li class='item-1'>1234</li><li>1235</li><li class='item-2'>
      123sdg</li><li>12水电费3</li></ul></div>"""

doc=pq(text)
print(doc('#ul1'))
item=doc('#ul1')
print(item.find('li'))
print(item.children('.active'))


#节点的遍历  items()

doc=pq(text)
print(doc('li').items())
for i,it  in enumerate(doc('li').items()):
    print(i,it)



"""
获取属性、text信息

.attr('href'),text()
获取内部html  .html()
"""


"""操作节点
addClass 和 removeClass  

除了操作 class 这个属性外，也可以用 attr （）方法对属性进行操作 。 此外，还可以用 text()
和 html （）方法来改变节点内部的内容


移除节点：remove
"""