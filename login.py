
import webbrowser
import sys
import os
sys.path.append('/Users/z001shw/Downloads/Work/Stocks')
url = 'https://trading.axisdirect.in/ordersbook/equity/book?showType=H&pageType=equity'
url = 'https://trade.axisdirect.co.in//homepage/Intermediate.jsp'

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

webbrowser.get(chrome_path).open(url)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(executable_path='/Users/z001shw/Downloads/Work/Stocks/chromedriver')
driver.get('https://login.axisdirect.in/')
text_area = driver.find_element_by_id('LoginUserForm_user_name')
text_area.send_keys(str('yashaswihv88'))

text_area = driver.find_element_by_id('LoginUserForm_password')
text_area.send_keys(str('Apr2019@1234'))

text_area = driver.find_element_by_id('LoginUserForm_date')
text_area.send_keys(str('16'))

text_area = driver.find_element_by_id('LoginUserForm_month')
text_area.send_keys(str('01'))

text_area = driver.find_element_by_id('LoginUserForm_year')
text_area.send_keys(str('1988'))


python_button = driver.find_elements_by_xpath('//*[@id="loginButtonM"]')[0]
python_button.click()

# windowHandles = driver.window_handles
# print(windowHandles)
# print(dir(windowHandles))
# driver.switch_to.window(windowHandles[0])

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='bodycontent']/div["
                                              "4]/div[2]/div/div[2]/div["
                                              "4]/div[2]"))).click()
windowHandles = driver.window_handles
print(windowHandles)
driver.switch_to.window(windowHandles[1])

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body"))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='MobileMenu']/div[2]/ul/li[1]"))).click()
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='inner-content-div']/div[1]/div/div[2]/p[1]"))).click()


from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.click(elem).perform()

# alert_obj = driver.switch_to.alert
# alert_obj.dismiss()
#
# python_button = driver.find_elements_by_xpath("//li[@class='tbuttonapi' and "
#                                               "@instrument-type='equity' and @product-type='cash']")[0]
# python_button.click()
