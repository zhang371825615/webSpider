from selenium import webdriver
from selenium.webdriver.common.by import  By
import  time

"""find_element_by_xpath的使用方法 find_elements_by_tag_name 多个  \ find_element_by_tag_name 获取第一个
"""


browser=webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chromedriver.exe')

main_page=browser.get('https://www.taobao.com')


print(browser.find_elements_by_xpath('//ul'))#找到当前文档内ul的所有元素

print(browser.find_elements_by_tag_name('li'))#获取多个
print(browser.find_element_by_tag_name('li'))#获取第一个