from  selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from  urllib.parse import  quote
from selenium.common.exceptions import TimeoutException

"""

抓取淘宝list 页面
"""
browser=webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chromedriver.exe')
wait = WebDriverWait(browser, 10)
domain='https://s.taobao.com/search?imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200924&ie=utf8&q='
keyWord='IPDA'


def get_page(page):
    '按照页码抓取'
    try:
        browser.get(domain+quote(keyWord))
        if page>1:
            input=wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,'.input.J_Input'))
            submit=wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,'.btn.J_Submit'))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.presence_of_element_located(By.ID,'mainsrp-itemlist'))
        print(browser.find_element_by_id('mainsrp-itemlist'))
    except TimeoutException:
          get_page(page)


get_page(1)









