from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.alert import Alert

url = 'http://103.8.112.44/hrms_ui'
path = 'C:\driver/chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(url)
time.sleep(5)


driver.maximize_window()

form = driver.find_element_by_xpath('//form[@name="form"]')
username = form.find_element_by_xpath('//input[@id="username"]')
password = form.find_element_by_xpath('//input[@id="password"]')
username.send_keys("IAI000052")
password.send_keys("12345")
time.sleep(1)
login = form.find_element_by_xpath('//button[@type="submit"]')
login.click()
time.sleep(1)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
DMS = driver.find_element_by_xpath('//*[@id="menulist"]/li[12]/a')
DMS.click()
time.sleep(1)
upload = driver.find_element_by_xpath('//*[@id="menulist"]/li[12]/ul/li[1]/a')
upload.click()
time.sleep(1)
filename = driver.find_element_by_xpath('//input[@id="File_name"]')
filename.send_keys('DEmo')
time.sleep(1)
selectdpt = driver.find_element_by_xpath('//select[@id="select_dept"]')
selectdpt.click()
selectdpt.send_keys('Production-Demo')
selectdpt.click()
version = driver.find_element_by_xpath('//select[@id="phone_num"]')
version.click()
version.send_keys('V1')
version.click()
time.sleep(1)
author = driver.find_element_by_xpath('//select[@id="select_author"]')
author.click()
author.send_keys('Zeeshan Ahmad - Implementations')
author.click()
time.sleep(1)
secretkey = driver.find_element_by_xpath('//select[@id="Secret_key"]')
secretkey.click()
secretkey.send_keys('Production-Demo')
secretkey.click()
time.sleep(1)
expirery = driver.find_element_by_xpath('//input[@id="expairy"]')
expirery.send_keys('03/10/2022')
time.sleep(1)
chosefile = driver.find_element_by_xpath('//input[@name="my_file"]')
chosefile.send_keys('D:\demo.txt')
time.sleep(1)
submit = driver.find_element_by_xpath('//button[@name="btn_submit"]')
submit.click()
time.sleep(1)
decending = driver.find_element_by_xpath('//*[@id="manageAQMSTable_wrapper"]/div[2]/div[1]/div/table/thead/tr/th[1]')
decending.click()
time.sleep(5)
search = driver.find_element_by_xpath('//input[@type="search"]')
search.send_keys('234')
time.sleep(5)
comnts = driver.find_element_by_xpath('//a[@class="pointer"]')
comnts.click()
time.sleep(1)
comntss = driver.find_element_by_xpath('//textarea[@name="d_comments"]')
comntss.click()
comntss.send_keys('qwertyuiolkjhgfdsdfghjkl,mnbvcxzxcvbnjytredscvbhytrd')
time.sleep(1)
submit = driver.find_element_by_xpath('//button[@type="submit"]')
submit.click()
time.sleep(1)
treeview = driver.find_element_by_xpath('//*[@id="sec1"]/div/div[1]/a')
treeview.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,2000)","")
time.sleep(2)
interns = driver.find_element_by_xpath('//a[@rel="D:/xampp/htdocs/hrms/uploads/Department/Implementation/"]')
interns.click()
time.sleep(1)
fileclick = driver.find_element_by_xpath('//a[@rel="D:/xampp/htdocs/hrms/uploads/Department/Implementation/TEST_V1.xlsx"]')
fileclick.click()
time.sleep(1)
# driver.execute_script("window.scrollBy(0,600)","")
# time.sleep(2)
# home = driver.find_element_by_xpath('/html/body/div/div[1]/section[1]/ol/li[1]/a')
# home.click()
# time.sleep(1)
###################ticket management###############################
sidebar = driver.find_element_by_xpath('//a[@class="sidebar-toggle"]')
sidebar.click()
time.sleep(1)
ticket = driver.find_element_by_xpath('//*[@id="menulist"]/li[7]/a')
ticket.click()
time.sleep(1)
ticketmanagement = driver.find_element_by_xpath('//*[@id="menulist"]/li[7]/ul/li/a')
ticketmanagement.click()
time.sleep(1)
selectissue = driver.find_element_by_xpath('//select[@id="issue_type"]')
selectissue.click()
selectissue.send_keys('Broken Items Issue - Admin')
selectissue.click()
time.sleep(1)
status = driver.find_element_by_xpath('//select[@id="status"]')
status.click()
status.send_keys('Pending ')
status.click()
time.sleep(1)
conmnts = driver.find_element_by_xpath('//textarea[@id="description"]')
conmnts.click()
conmnts.send_keys('waiting for some days this issue did not be resolved')
submit = driver.find_element_by_xpath('//button[@id="btn_submit"]')
submit.click()
time.sleep(1)
selectcriteria = driver.find_element_by_xpath('//select[@id="issue_search"]')
selectcriteria.click()
selectcriteria.send_keys('Broken Items Issue - Admin')
selectcriteria.click()
find = driver.find_element_by_xpath('//button[@id="btn_search"]')
find.click()
time.sleep(1)
logout = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/a/span[1]')
logout.click()
time.sleep(1)
log = driver.find_element_by_xpath('//a[@href="http://103.8.112.44/hrms/login/logout"]')
log.click()
time.sleep(1)