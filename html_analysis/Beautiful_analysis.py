"""
Beautiftful Soup解析器


lxmlHTML解析器   BeautifulSoup(markup,'lxml') 速度快 、文档容错能力强 ，需要安装C语言库

"""

# coding:utf-8
#from  bs4  import BeautifulSoup
import requests
from bs4 import BeautifulSoup

soup=BeautifulSoup('<p>asdad</p>','lxml')
print(soup.p.string)


htmlStr="""<html>
           
           <head>headads1<title name='asdad' class='ad12 123分'>标题</title></head>
          <div id="helpsmenu-container" style="display: none;">
            <div class="helpsmenu-selfinfo"></div>
            <ul class="helpsmenu">
                <li><a href="javascript:;" class="about_version">版本信息</a></li>
                <li><a href="javascript:;" class="help">桌面指引</a></li>
                <li><a href="javascript:;" class="about_hotkey">快捷键说明</a></li>
            </ul>
        </div></html>"""

soup=BeautifulSoup(htmlStr,'lxml')
soup.prettify()
print(soup.title) #<title name="asdad">标题</title>
print(soup.title.string) #标题
print('name',soup.head.name)#标签名称:head
print('attrs',soup.title.attrs)#{'name': 'asdad', 'class': ['ad12']}
print('attr name',soup.title.attrs['name'])#标签名称:asdad
print('attr class',soup.title.attrs['class'])#['ad12', '123分']



#获取所有直接子节点 contents 直接子节点
print(soup.ul.contents)#['\n', <li><a class="about_version" href="javascript:;">版本信息</a></li>, '\n', <li><a class="help" href="javascript:;">桌面指引</a></li>, '\n', <li><a class="about_hotkey" href="javascript:;">快捷键说明</a></li>, '\n']

print(soup.div.children)
for i, child in enumerate(soup.div.children):
    print(i, child)

print('********************************************')
#descendants获取所有子孙节点
print(soup.div.descendants)
for i, child in enumerate(soup.div.descendants):
    print(i, child)


print('********************************************')

#输出父节点及其内容
print(soup.ul.parent)
"""<div id="helpsmenu-container" style="display: none;">
<div class="helpsmenu-selfinfo"></div>
<ul class="helpsmenu">
<li><a class="about_version" href="javascript:;">版本信息</a></li>
<li><a class="help" href="javascript:;">桌面指引</a></li>
<li><a class="about_hotkey" href="javascript:;">快捷键说明</a></li>
</ul>
</div>"""

#find_all(narne , attrs , recursive , text , **kwargs)
print(soup.find_all(name='a',attrs={'class':'help'}))




