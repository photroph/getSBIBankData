import getpass
import os.path
from selenium import webdriver

print('username :', end='')
u = input()
p = getpass.getpass()

# access to login page
driver = webdriver.Chrome(executable_path=os.path.expanduser('~')+'/workspace/scripts/getSBIBankData/chromedriver')
login_page_url = "https://www.netbk.co.jp/contents/pages/wpl010101/i010101CT/DI01010210"
# fill login form
driver.get(login_page_url)
el = driver.find_element_by_id('userName')
el.clear
el.send_keys(u)
el = driver.find_element_by_id('loginPwdSet')
el.clear
el.send_keys(p)
# login
driver.find_element_by_css_selector('button.m-btnEm-l').click()

# access balance page
driver.implicitly_wait(2)
balance_page_url = driver.find_element_by_css_selector('a.m-icon-ps_balance').get_attribute('href')
driver.get(balance_page_url)
# get balance
print(driver.find_element_by_css_selector('li.m-zandaka-item span.m-zandaka-number').text)