from selenium import webdriver
from selenium.webdriver.common.by import  By
import  time



browser=webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chromedriver.exe')

browser.get('https://www.taobao.com')

#lis = browser.find_element_by_css_selector('.service-bd li')

#input=browser.find_element_by_id('q')
#input.send_keys('iphone')
#button= browser.find_element_by_class_name('btn-search')
#button.click()



"""
获取文本信息: 
位置信息： {'x': 235, 'y': 154}
tag_name： input
文本框大小 {'height': 36, 'width': 472}
"""
input=browser.find_element_by_id('q')
print('获取文本信息:',input.text)
print('位置信息：',input.location)
print('tag_name：',input.tag_name)
print('文本框大小',input.size)

"获取左侧清单的中的商品分类信息"

lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
for ele in lis:
    alist=ele.find_elements_by_xpath('a') #获取列表，ele.find_elements_by_tagName'a')这个方法只能获取一个
    tag_text=''
    for a_tag in alist:
        tag_text=tag_text+'###'+a_tag.text
    print(tag_text)
#print(lis)




time.sleep(5)
browser.close()

