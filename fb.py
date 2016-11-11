import time
import getpass
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def get_title(driver):
    html_page = driver.page_source
    soup = BeautifulSoup(html_page,'html.parser')
    print(soup.title.string+"\n")
    return soup.title.string

binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
url = "https://facebook.com"

while True:
    driver.get(url)
    time.sleep(2)
    get_title(driver)

    eMail = input("Enter your Email Id or Mobile No. to Login\n")
    pAss = getpass.getpass("Enter your password\n")

    email = driver.find_element_by_name("email")
    email.send_keys(eMail)
    password = driver.find_element_by_name("pass")
    password.send_keys(pAss)

    login = driver.find_element_by_css_selector("#u_0_l")
    login.click()
    time.sleep(5)

    if get_title(driver) != "Log in to Facebook | Facebook":
        print("You are logged in now\n")

        pp = input("Enter your Status\n")
        # status = driver.find_element_by_xpath('//textarea[@class="uiTextareaAutogrow _3en1" or @class="uiTextareaAutogrow _3en1 _480e"]')
        status = driver.find_element_by_xpath('//textarea[contains(@class, "uiTextareaAutogrow")]')

        status.send_keys(pp)
        button = driver.find_element_by_xpath('//div[@class="clearfix"]/div[contains(@class, "rfloat")]/div/button[@type="submit" and @value="1"]')
        button.click()
        time.sleep(5)
        print("Your Status : '"+pp+"' has been uploaded!\n")
        driver.quit()
        break

    else:
        print("Invalid Email Id or Password, Try Login Again\nCtrl+C to exit the script\n")