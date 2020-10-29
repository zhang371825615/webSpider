from  selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import  time
#r'C:\Dpapp\Chrome\ChromePortable\ChromePortable.exe'

#option.binary_location=r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chrome.exe'
#C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chrome.exe
browser=webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chromedriver.exe')


try:
    browser.get('https://wwww.baidu.com')
    input=browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_right')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(5)
except EOFError as e:
     print(e)
finally:
    browser.close()




