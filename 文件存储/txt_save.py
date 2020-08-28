import  requests
from  pyquery import PyQuery as pq

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
}
url='https://www.zhihu.com/explore'
html=requests.get(url,headers=headers).text
doc=pq(html)
items=doc(".ExploreHomePage-ContentSection-body .ExploreHomePage-specials .ExploreHomePage-specialCard .ExploreSpecialCard-contentList .ExploreSpecialCard-contentItem").items()
print(items)
for  it in items:
   # print("contentTag:",it.find('.ExploreSpecialCard-contentTag').text(),'contentTitle:',it.find('.ExploreSpecialCard-contentTitle').text())
    contentTag=it.find('.ExploreSpecialCard-contentTag').text()
    contentTitle=it.find('.ExploreSpecialCard-contentTitle').text()
    file = open('explore.txt','a',encoding='utf-8')  #追加的方式寫入
    file.write('\n'.join([contentTag,contentTitle]))
    file.write(' \n '+'='*50 +'\n')
    file.close()

