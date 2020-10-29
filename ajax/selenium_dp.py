from selenium import webdriver
import  time



browser=webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chromedriver.exe')
browser.get('http://boas.deppon.com:8080/')
finger=browser.find_element_by_class_name('finger')
finger.click()
userid_input=browser.find_element_by_name('empcode')
userid_input.send_keys('198777')
pass_input=browser.find_element_by_class_name('pass-word')
pass_input.send_keys('zjy0011@@')
smile_ionic=browser.find_element_by_class_name('feeling1')
smile_ionic.click()
go_work=browser.find_element_by_class_name('kq-onwork')
go_work.click()
time.sleep(5)


sub_ok=browser.find_element_by_css_selector('.kq-alert3 .kq-ok')
sub_ok.click()

browser.close()


