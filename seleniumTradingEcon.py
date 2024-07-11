from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()

url = "https://tradingeconomics.com/" +  + "/bank-lending-rate"

browser.get(url)
try:
    elem = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ctl00_ctl00_PanelPeers > div > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    print(f'The interest rate is {elem.text}')
except:
    print('Unable to extract interest rate.')

browser.quit()