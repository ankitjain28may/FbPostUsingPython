import time
import platform
import getpass
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.phantomjs.webdriver import WebDriver


def get_title(driver):
    html_page = driver.page_source
    soup = BeautifulSoup(html_page,'html.parser')
    print(soup.title.string+"\n")
    return soup.title.string

if platform.system() == 'Windows':
    pathr = 'C:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
else:
    pathr = './phantomjs'
driver = webdriver.PhantomJS(pathr, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
url = "https://mbasic.facebook.com/"

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

    login = driver.find_element_by_name("login")
    login.click()
    time.sleep(5)
    

    if get_title(driver) != "Log in to Facebook | Facebook":
        print("You are logged in now\n")
        #afterlogin the url changes so we need to set the url again
        driver.get(url)

        pp = input("Enter your Status\n")
        status = driver.find_element_by_name("xc_message")

        status.send_keys(pp)
        button = driver.find_element_by_name("view_post")
        button.click()
        time.sleep(5)
        print("Your Status : '"+pp+"' has been uploaded!\n")
        driver.quit()
        break

    else:
        print("Invalid Email Id or Password, Try Login Again\nCtrl+C to exit the script\n")
