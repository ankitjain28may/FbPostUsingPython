import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


def get_title(driver):
    html_page = driver.page_source
    soup = BeautifulSoup(html_page,'html.parser')
    print(soup.title.string+"\n")


url = "https://facebook.com"

driver = webdriver.Firefox()
driver.get(url)
time.sleep(2)
get_title(driver)

eMail = input("Enter your Email Id or Mobile No. to Login\n")
pAss = input("Enter your password\n")

email = driver.find_element_by_name("email")
email.send_keys(eMail)
password = driver.find_element_by_name("pass")
password.send_keys(pAss)

login = driver.find_element_by_css_selector("#u_0_l")
login.click()
print("You are logged in now\n")
time.sleep(5)

get_title(driver)
pp = input("Enter your Status\n")
status = driver.find_element_by_xpath('//textarea[@class="uiTextareaAutogrow _3en1" or @class="uiTextareaAutogrow _3en1 _480e"]')
status.send_keys(pp)

button = driver.find_element_by_xpath('//button[@type="submit" and @class="_42ft _4jy0 _ej1 _4jy3 _4jy1 selected _51sy" and @value="1"]')
button.click()
print("Your Status : '"+pp+"' has been uploaded!\n")
driver.quit()
