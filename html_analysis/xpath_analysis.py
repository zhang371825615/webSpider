"""
Xpath包解析
title[@lang='eng'] tile标签中lang属性为eng的节点
"""
# encoding=utf8

from lxml import  html

etree = html.etree

text="""<div><ul><li class='item-0'>123<a href='www.baidu.com'>百度</a></li><li class='item-1'>1234</li><li>1235</li><li class='item-2'>
      123sdg</li><li>12水电费3</li></ul></div>"""

html=etree.HTML(text)

result=etree.tostring(html,encoding='utf-8', pretty_print=True)

#print(result.decode('utf-8'))



html = etree.parse('./德邦e站 - 论坛首页.html', etree.HTMLParser())

result= etree.tostring(html,encoding='utf-8', pretty_print=True)
#print(result)
#print(result.decode('utf-8'))


html = etree.parse('./test.html')

result=(etree.tostring(html, encoding="utf-8", pretty_print=True, method="html"))


print(result.decode("utf-8"))
print(result)






result = html.xpath("//a[@href='www.baidu.com']/../@class")
print(result)

result = html.xpath("//li[@class='item-1']/text()")

result = html.xpath("//li[@class='item-0']/a/@href")

#<li class="dev1 df calss2"><a href='www.baidu2.com'>百度2</a></li>
#class属性存在多值,多属性匹配result = html.xpath("//li[@class='dev1']/")无法匹配
result = html.xpath("//li[contains(@class,'df') and @name='zhangsan']/a/text()")

print('contains class多值,且多属性：',result)