import time
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib.request
import json
import validators
from selenium.webdriver.common.keys import Keys



def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


header={'User-Agent':"Mozilla/6.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}

print("Facebook")

url = "https://facebook.com"

print(url)



driver = webdriver.Firefox()
driver.get(url)

html_page = driver.page_source

soup = BeautifulSoup(html_page,'html.parser')
print(soup.title.string)

eMail = input("Enter your email Id\n")
pAss = input("Enter your password\n")

email = driver.find_element_by_name("email")
email.send_keys(eMail)

password = driver.find_element_by_name("pass")
password.send_keys(pAss)



start = driver.find_element_by_css_selector("#u_0_l")
start.click()

time.sleep(5)
pp = input("Enter your Status\n")



post = driver.find_element_by_xpath('//textarea[@class="uiTextareaAutogrow _3en1"]')
post.send_keys(pp)

NEXT_BUTTON_XPATH = '//button[@type="submit" and @class="_42ft _4jy0 _ej1 _4jy3 _4jy1 selected _51sy" and @value="1"]'
button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
button.click()

# Click_BUTTON_XPATH = '//form[@method="post" and @name="formNTQxNTQ1"]/input[2]'
# _inputs = driver.find_element_by_xpath(Click_BUTTON_XPATH)
# _inputs.click();
