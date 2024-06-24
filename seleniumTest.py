from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
    # for e in elem:
    #     print(e.text)
except:
    print('Was not able to find an element with that name.')