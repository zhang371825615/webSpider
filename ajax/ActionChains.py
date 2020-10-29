from selenium.webdriver import ActionChains
from selenium import webdriver

"""动作链，拖拽"""
browser = webdriver.Chrome(r'C:\Dpapp\Chrome\ChromePortable\App\Google Chrome\chromedriver.exe')
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame ('iframeResult')
source = browser.find_element_by_css_selector('.ui-draggable')
target = browser.find_element_by_css_selector('.ui-droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()








