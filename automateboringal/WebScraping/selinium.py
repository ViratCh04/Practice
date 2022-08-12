import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# #quoteSearchPopupWrapper

browser = webdriver.Firefox()
browser.get('https://monkeytype.com')
# Skips past the obligatory accept cookies while controlling browser remotely
WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div[1]'))).click()
# finds quote button
elem = browser.find_element(By.CSS_SELECTOR, 'div.mode:nth-child(2) > div:nth-child(1) > div:nth-child(3)')
elem.click()
# finds search button
elem = browser.find_element(By.CSS_SELECTOR, 'div.textButton:nth-child(7) > i:nth-child(1)')
elem.click()
# finds search box
searchElement = browser.find_element(By.CSS_SELECTOR, '#searchBox')
searchElement.send_keys('Cat')
# searchElement.submit()            # not needed here
time.sleep(5)
elem = browser.find_element(By.CSS_SELECTOR, '#quoteSearchPopupWrapper')
elem.click()
# browser.back()        # goes back a page
# browser.forward()     # forwards a page
time.sleep(3)
browser.refresh()
time.sleep(3)
browser.quit()
