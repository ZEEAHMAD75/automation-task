from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.alert import Alert
import mouse
from selenium.webdriver.common.keys import Keys
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


##############################TMS##################################################

sidebar = driver.find_element_by_xpath('//a[@class="sidebar-toggle"]')
sidebar.click()
time.sleep(1)
clickon = driver.find_element_by_xpath('//*[@id="menulist"]/li[9]/a')
clickon.click()
upload = driver.find_element_by_xpath('//*[@id="menulist"]/li[9]/ul/li[1]/a')
upload.click()
form = driver.find_element_by_xpath('//form[@name="form"]')
file = driver.find_element_by_xpath('//input[@id="File_name"]')
file.send_keys('Davd-waise-testing')
time.sleep(1)
assigne = driver.find_element_by_xpath('//*[@id="resu_assignee"]')
assigne.click()
assigne.send_keys('Qiran Sohail')
assigne.click()
time.sleep(1)
duedate = driver.find_element_by_xpath('//input[@id="datepicker"]')
mouse.move(680,330, absolute=True , duration=4)
time.sleep(1)
mouse.click(button='left')
time.sleep(5)
duedate.send_keys(Keys.RIGHT)
time.sleep(1)
duedate.send_keys(Keys.RIGHT)
time.sleep(1)
duedate.send_keys(Keys.RIGHT)
time.sleep(1)
duedate.send_keys(Keys.RIGHT)
time.sleep(1)
duedate.send_keys(Keys.ENTER)
time.sleep(1)
priority = driver.find_element_by_xpath('//select[@id="resu_proirity"]')
priority.click()
priority.send_keys('High')
time.sleep(1)
status = driver.find_element_by_xpath('//select[@id="resu_Status"]')
status.click()
status.send_keys('Scheduled')
time.sleep(1)
phone = driver.find_element_by_xpath('//input[@id="phone_num"]')
phone.click()
phone.send_keys('01123456781')
time.sleep(1)
depart = driver.find_element_by_xpath('//select[@id="select_dept"]')
depart.click()
depart.send_keys('Production-Demo')
time.sleep(1)
desig = driver.find_element_by_xpath('//select[@id="select_desg"]')
desig.click()
desig.send_keys('Production-intern-DEMO')
time.sleep(1)
grade = driver.find_element_by_xpath('//select[@id="grade"]')
grade.click()
grade.send_keys('A')
time.sleep(1)
sendtomanager = driver.find_element_by_xpath('//select[@id="send_manager"]')
sendtomanager.click()
sendtomanager.send_keys('Sumeya Anjum')
sendtomanager.click()
time.sleep(1)
shedate = driver.find_element_by_xpath('//*[@id="datepicker1"]')
mouse.move(1310,400, absolute=True , duration=5)
time.sleep(1)
mouse.click(button='left')
time.sleep(5)
shedate.send_keys(Keys.RIGHT)
time.sleep(1)
shedate.send_keys(Keys.RIGHT)
time.sleep(1)
shedate.send_keys(Keys.ENTER)
time.sleep(1)
file = driver.find_element_by_xpath('//input[@type="file"]')
file.send_keys('D:\demo.txt')
time.sleep(1)
comnts = driver.find_element_by_xpath('//textarea[@id="comments"]')
comnts.click()
comnts.send_keys('only for testing purpose')
time.sleep(1)
submit = driver.find_element_by_xpath('//input[@type="submit"]')
submit.click()
time.sleep(1)
sidebar = driver.find_element_by_xpath('//a[@class="sidebar-toggle"]')
sidebar.click()
time.sleep(1)
clickon = driver.find_element_by_xpath('//*[@id="menulist"]/li[9]/a')
clickon.click()
time.sleep(1)
viewresume = driver.find_element_by_xpath('//*[@id="menulist"]/li[9]/ul/li[2]/a')
viewresume.click()
time.sleep(20)
search = driver.find_element_by_xpath('//input[@type="search"]')
search.click()
search.send_keys('2842')
time.sleep(1)
export = driver.find_element_by_xpath('//*[@id="sec1"]/div/div[1]/a')
export.click()
time.sleep(1)
ofpageedit = driver.find_element_by_xpath('//*[@id="manageHRMSTable"]/tbody/tr[1]/td[12]/a[3]')
ofpageedit.click()
time.sleep(1)
status = driver.find_element_by_xpath('//select[@id="resu_Status"]')
status.click()
status.send_keys('Hired')
time.sleep(1)
status.click()
time.sleep(1)
hiredate = driver.find_element_by_xpath('//*[@id="datepicker1"]')
mouse.move(1310,400, absolute=True , duration=5)
time.sleep(1)
mouse.click(button='left')
time.sleep(5)
hiredate.send_keys(Keys.RIGHT)
time.sleep(1)
hiredate.send_keys(Keys.RIGHT)
time.sleep(1)
hiredate.send_keys(Keys.ENTER)
time.sleep(1)
sendtomanager = driver.find_element_by_xpath('//*[@id="send_manager"]')
sendtomanager.click()
sendtomanager.send_keys('Sumeya Anjum')
sendtomanager.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
coments = driver.find_element_by_xpath('//*[@id="comments"]')
coments.click()
coments.send_keys('ONLY FOR TESTING PURPOSE')
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
addcomnt = driver.find_element_by_xpath('//*[@id="sec1"]/div/div[2]/form/div[1]/div[3]/div/div/input')
addcomnt.click()
time.sleep(1)
upload = driver.find_element_by_xpath('//*[@id="fullname"]/input')
upload.click()
time.sleep(15)
sidebar = driver.find_element_by_xpath('//a[@class="sidebar-toggle"]')
sidebar.click()
time.sleep(1)
clickon = driver.find_element_by_xpath('//*[@id="menulist"]/li[9]/a')
clickon.click()
time.sleep(1)
report = driver.find_element_by_xpath('//*[@id="menulist"]/li[9]/ul/li[3]/a')
report.click()
time.sleep(1)
formdate = driver.find_element_by_xpath('//input[@id="datepicker4"]')
formdate.send_keys('02/22/2022')
time.sleep(1)
todate = driver.find_element_by_xpath('//*[@id="datepicker5"]')
todate.send_keys('03/06/2022')
time.sleep(1)
assien = driver.find_element_by_xpath('//select[@id="assignee"]')
assien.click()
assien.send_keys('Qiran Sohail')
time.sleep(1)
priority = driver.find_element_by_xpath('//select[@id="resu_proirity"]')
priority.click()
priority.send_keys('High')
time.sleep(1)
status = driver.find_element_by_xpath('//select[@id="resu_Status"]')
status.click()
status.send_keys('hired')
status.click()
time.sleep(1)
submit = driver.find_element_by_xpath('//button[@id="btn_submit"]')
submit.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
find = driver.find_element_by_xpath('//input[@type="search"]')
find.send_keys('2842')
time.sleep(1)
export = driver.find_element_by_xpath('//a[@id="btn_export"]')
export.click()
time.sleep(1)


#####################################EMS######################################################################

clickon = driver.find_element_by_xpath('//*[@id="menulist"]/li[5]/a')
clickon.click()
time.sleep(1)
viewemp = driver.find_element_by_xpath('//*[@id="menulist"]/li[5]/ul/li[2]/a')
viewemp.click()
time.sleep(1)
search = driver.find_element_by_xpath('//*[@id="manageHRMSTable_filter"]/label/input')
search.click()
search.send_keys('1215')
time.sleep(3)
onpageedit = driver.find_element_by_xpath('//*[@id="manageHRMSTable"]/tbody/tr/td[11]/a[1]')
onpageedit.click()
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="e_name"]').click()
name = driver.find_element_by_xpath('//*[@id="e_name"]').clear()
name = driver.find_element_by_xpath('//*[@id="e_name"]')
name.send_keys('TESTING-DAVID')
time.sleep(2)
address = driver.find_element_by_xpath('//*[@id="e_address"]').click()
address = driver.find_element_by_xpath('//*[@id="e_address"]').clear()
address = driver.find_element_by_xpath('//*[@id="e_address"]')
address.send_keys('DHA LAHORE')
time.sleep(1)
city = driver.find_element_by_xpath('//*[@id="e_city"]').click()
city = driver.find_element_by_xpath('//*[@id="e_city"]').clear()
city = driver.find_element_by_xpath('//*[@id="e_city"]')
city.send_keys('LAHORE')
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="updateEmployeeForm"]/div[2]/button[2]')
submit.click()
time.sleep(1)
search = driver.find_element_by_xpath('//*[@id="manageHRMSTable_filter"]/label/input')
search.click()
search.send_keys('1215')
time.sleep(5)
vieweemp = driver.find_element_by_xpath('//*[@id="manageHRMSTable"]/tbody/tr/td[11]/a[2]')
vieweemp.click()
time.sleep(5)
personalinfo = driver.find_element_by_xpath('//*[@id="headingTwo"]/h4/a')
personalinfo.click()
time.sleep(1)
title = driver.find_element_by_xpath('//*[@id="Title"]').click()
title = driver.find_element_by_xpath('//*[@id="Title"]').clear()
title = driver.find_element_by_xpath('//*[@id="Title"]')
title.send_keys('MR')
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="first_name"]').click()
name = driver.find_element_by_xpath('//*[@id="first_name"]').clear()
name = driver.find_element_by_xpath('//*[@id="first_name"]')
name.send_keys('TESTING-DAVID')
time.sleep(1)
gender = driver.find_element_by_xpath('//*[@id="gender"]')
gender.click()
gender.send_keys('male')
gender.click()
time.sleep(1)
country = driver.find_element_by_xpath('//*[@id="country"]')
country.click()
country.send_keys('Pakistan')
country.click()
time.sleep(1)
nationality = driver.find_element_by_xpath('//*[@id="nationality"]')
nationality.click()
nationality.send_keys('Pakistan')
nationality.click()
time.sleep(1)
town = driver.find_element_by_xpath('//*[@id="town"]').click()
town = driver.find_element_by_xpath('//*[@id="town"]').clear()
town = driver.find_element_by_xpath('//*[@id="town"]')
town.send_keys('ICHRA')
time.sleep(1)
city = driver.find_element_by_xpath('//*[@id="city"]').click()
city = driver.find_element_by_xpath('//*[@id="city"]').clear()
city = driver.find_element_by_xpath('//*[@id="city"]')
city.send_keys('LAHORE')
time.sleep(1)
state = driver.find_element_by_xpath('//*[@id="state"]')
state.click()
state.send_keys('Punjab')
state.click()
time.sleep(1)
tmpaddress= driver.find_element_by_xpath('//*[@id="address"]').click()
tmpaddress= driver.find_element_by_xpath('//*[@id="address"]').clear()
tmpaddress= driver.find_element_by_xpath('//*[@id="address"]')
tmpaddress.send_keys('DHA LAHORE')
time.sleep(1)
permaddress = driver.find_element_by_xpath('//*[@id="permanent_address"]').click()
permaddress = driver.find_element_by_xpath('//*[@id="permanent_address"]').clear()
permaddress = driver.find_element_by_xpath('//*[@id="permanent_address"]')
permaddress.send_keys('DHA LAHORE')
time.sleep(1)
pho = driver.find_element_by_xpath('//*[@id="phone"]')
pho.click()
pho.send_keys('03211212121')
time.sleep(1)
mob = driver.find_element_by_xpath('//*[@id="mobile"]')
mob.click()
mob.send_keys('03211212121')
time.sleep(1)
email = driver.find_element_by_xpath('//*[@id="email"]').click()
email = driver.find_element_by_xpath('//*[@id="email"]').clear()
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('DAVID-WAISE@gmail.com')
time.sleep(1)
cnic = driver.find_element_by_xpath('//*[@id="Emp_nic"]')
cnic.click()
cnic.send_keys('352021234567876543')
time.sleep(1)
remakrs = driver.find_element_by_xpath('//*[@id="Remarks"]').click()
remakrs = driver.find_element_by_xpath('//*[@id="Remarks"]').clear()
remakrs = driver.find_element_by_xpath('//*[@id="Remarks"]')
remakrs.send_keys('4')
time.sleep(1)
driver.execute_script("window.scrollBy(0,300)","")
time.sleep(2)
salaryinfo = driver.find_element_by_xpath('//*[@id="headingThree"]/h4/a')
salaryinfo.click()
time.sleep(1)
bank = driver.find_element_by_xpath('//*[@id="Bank_Account_No"]').click()
bank = driver.find_element_by_xpath('//*[@id="Bank_Account_No"]').clear()
bank = driver.find_element_by_xpath('//*[@id="Bank_Account_No"]')
bank.send_keys('0987654321')
bank.click()
time.sleep(1)
basicsal = driver.find_element_by_xpath('//*[@id="Basic_Salary"]').click()
basicsal = driver.find_element_by_xpath('//*[@id="Basic_Salary"]').clear()
basicsal = driver.find_element_by_xpath('//*[@id="Basic_Salary"]')
basicsal.send_keys('0,000')
time.sleep(1)
paystatus = driver.find_element_by_xpath('//*[@id="pay_status"]')
paystatus.click()
paystatus.send_keys('Active')
paystatus.click()
time.sleep(1)
payfreque = driver.find_element_by_xpath('//*[@id="pay_Frequency"]')
payfreque.click()
payfreque.send_keys('Month')
payfreque.click()
time.sleep(1)
jobtype = driver.find_element_by_xpath('//*[@id="job_type"]')
jobtype.click()
jobtype.send_keys('FTE')
jobtype.click()
time.sleep(1)
familyinfo = driver.find_element_by_xpath('//*[@id="headingFour"]/h4/a')
familyinfo.click()
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="fam_name_one"]').click()
name = driver.find_element_by_xpath('//*[@id="fam_name_one"]').clear()
name = driver.find_element_by_xpath('//*[@id="fam_name_one"]')
name.send_keys('WISE')
time.sleep(1)
rela = driver.find_element_by_xpath('//*[@id="fam_relation_one"]').click()
rela = driver.find_element_by_xpath('//*[@id="fam_relation_one"]').clear()
rela = driver.find_element_by_xpath('//*[@id="fam_relation_one"]')
rela.send_keys('FATHER')
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="fam_name_two"]').click()
name = driver.find_element_by_xpath('//*[@id="fam_name_two"]').clear()
name = driver.find_element_by_xpath('//*[@id="fam_name_two"]')
name.send_keys('WISE')
time.sleep(1)
rela = driver.find_element_by_xpath('//*[@id="fam_relation_two"]').click()
rela = driver.find_element_by_xpath('//*[@id="fam_relation_two"]').clear()
rela = driver.find_element_by_xpath('//*[@id="fam_relation_two"]')
rela.send_keys('FATHER')
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="fam_name_three"]').click()
name = driver.find_element_by_xpath('//*[@id="fam_name_three"]').clear()
name = driver.find_element_by_xpath('//*[@id="fam_name_three"]')
name.send_keys('WISE')
name.click()
time.sleep(1)
rela = driver.find_element_by_xpath('//*[@id="fam_relation_three"]').click()
rela = driver.find_element_by_xpath('//*[@id="fam_relation_three"]').clear()
rela = driver.find_element_by_xpath('//*[@id="fam_relation_three"]')
rela.send_keys('FATHER')
rela.click()
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="emergency_name_one"]').click()
name = driver.find_element_by_xpath('//*[@id="emergency_name_one"]').clear()
name = driver.find_element_by_xpath('//*[@id="emergency_name_one"]')
name.send_keys('WISE')
time.sleep(1)
relation = driver.find_element_by_xpath('//*[@id="emergency_relation_one"]').click()
relation = driver.find_element_by_xpath('//*[@id="emergency_relation_one"]').clear()
relation = driver.find_element_by_xpath('//*[@id="emergency_relation_one"]')
relation.send_keys('FATHER')
time.sleep(1)
cont = driver.find_element_by_xpath('//*[@id="emergency_contact_one"]').click()
cont = driver.find_element_by_xpath('//*[@id="emergency_contact_one"]').clear()
cont = driver.find_element_by_xpath('//*[@id="emergency_contact_one"]')
cont.send_keys('032347654321')
time.sleep(1)
name = driver.find_element_by_xpath('//*[@id="emergency_name_two"]').click()
name = driver.find_element_by_xpath('//*[@id="emergency_name_two"]').clear()
name = driver.find_element_by_xpath('//*[@id="emergency_name_two"]')
name.send_keys('Gayle')
name.click()
time.sleep(1)
rela = driver.find_element_by_xpath('//*[@id="emergency_relation_two"]').click()
rela = driver.find_element_by_xpath('//*[@id="emergency_relation_two"]').clear()
rela = driver.find_element_by_xpath('//*[@id="emergency_relation_two"]')
rela.send_keys('Partner')
rela.click()
time.sleep(1)
cont = driver.find_element_by_xpath('//*[@id="emergency_contact_two"]').click()
cont = driver.find_element_by_xpath('//*[@id="emergency_contact_two"]').clear()
cont = driver.find_element_by_xpath('//*[@id="emergency_contact_two"]')
cont.send_keys('12345')
time.sleep(1)
driver.execute_script("window.scrollBy(0,700)","")
time.sleep(2)
sendmail = driver.find_element_by_xpath('//*[@id="heading"]/h4/a')
sendmail.click()
time.sleep(1)
hod = driver.find_element_by_xpath('//*[@id="hod_mail"]')
hod.click()
hod.send_keys('Sumeya Anjum')
hod.click()
time.sleep(1)
mail = driver.find_element_by_xpath('//*[@id="collapseFive"]/div/div[2]/div/input')
mail.click()
time.sleep(1)
cv = driver.find_element_by_xpath('//*[@id="inputGroupFile01"]')
cv.send_keys('D:\demo.txt')
time.sleep(1)
pic = driver.find_element_by_xpath('//*[@id="inputGroupFile02"]')
pic.send_keys('D:\demo.txt')
time.sleep(1)
cnic = driver.find_element_by_xpath('//*[@id="inputGroupFile03"]')
cnic.send_keys('D:\demo.txt')
time.sleep(1)
driver.execute_script("window.scrollBy(0,300)","")
time.sleep(2)
submit = driver.find_element_by_xpath('//*[@id="fullname"]/button')
submit.click()
time.sleep(1)





#################################ADMINISTATOR####################################################

sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
dash = driver.find_element_by_xpath('//*[@id="menulist"]/li[2]/a')
dash.click()
time.sleep(1)
brak = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[3]/button')
brak.click()
time.sleep(1)
short = driver.find_element_by_xpath('//*[@id="customRadio1"]')
short.click()
time.sleep(1)
long = driver.find_element_by_xpath('//*[@id="customRadio2"]')
long.click()
time.sleep(1)
full = driver.find_element_by_xpath('//*[@id="customRadio3"]')
full.click()
time.sleep(1)
emer = driver.find_element_by_xpath('//*[@id="customRadio4"]')
emer.click()
time.sleep(1)
can = driver.find_element_by_xpath('//*[@id="btn_close"]')
can.click()
i = 1
while i<=3:
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(2)
    i += 1
time.sleep(1)

sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
adminitator = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
adminitator.click()
time.sleep(1)
role = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[2]/a')
role.click()
time.sleep(1)
addrole = driver.find_element_by_xpath('//*[@id="form-role"]')
addrole.click()
addrole.send_keys('Testing production-Intern')
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(10)
search = driver.find_element_by_xpath('//*[@id="btn_search"]')
search.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(2)
decending = driver.find_element_by_xpath('//*[@id="manageAQMSTable_wrapper"]/div[2]/div[1]/div/table/thead/tr/th[1]')
decending.click()
time.sleep(5)
searchbar = driver.find_element_by_xpath('//*[@id="manageAQMSTable_filter"]/label/input')
searchbar.click()
searchbar.send_keys('161')
time.sleep(1)
edit = driver.find_element_by_xpath('//*[@id="manageAQMSTable"]/tbody/tr/td[6]/a[1]')
edit.click()
time.sleep(1)
savechanges = driver.find_element_by_xpath('//button[@type="submit"]')
savechanges.click()
time.sleep(5)
search = driver.find_element_by_xpath('//*[@id="btn_search"]')
search.click()
time.sleep(1)
searchbar = driver.find_element_by_xpath('//*[@id="manageAQMSTable_filter"]/label/input')
searchbar.click()
searchbar.send_keys('161')
time.sleep(1)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
adminitator = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
adminitator.click()
time.sleep(1)
access = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[3]/a')
access.click()
time.sleep(1)
roles = driver.find_element_by_xpath('//*[@id="form-roleid"]')
roles.click()
roles.send_keys('Testing production-Intern')
roles.click()
time.sleep(1)
moduels = driver.find_element_by_xpath('//*[@id="form-moduleid"]')
moduels.click()
moduels.send_keys('13-Attendance')
moduels.click()
time.sleep(1)
submoduel = driver.find_element_by_xpath('//*[@id="form-page"]')
submoduel.click()
submoduel.send_keys('Attendance Record')
submoduel.click()
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(5)
driver.execute_script("window.scrollBy(0,200)", "")
time.sleep(2)
selectrole = driver.find_element_by_xpath('//*[@id="form-roleid2"]')
selectrole.click()
selectrole.send_keys('Testing production-Intern')
selectrole.click()
time.sleep(1)
find = driver.find_element_by_xpath('//*[@id="btn_search"]')
find.click()
time.sleep(1)
edit = driver.find_element_by_xpath('//*[@id="manageAccessTable"]/tbody/tr/td[6]/a[1]')
edit.click()
time.sleep(1)
close = driver.find_element_by_xpath('//*[@id="btn_close"]')
close.click()
time.sleep(1)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
adminitator = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
adminitator.click()
time.sleep(1)
user = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[1]/a')
user.click()
time.sleep(1)

selectemp = driver.find_element_by_xpath('//*[@id="form-emp"]')
selectemp.click()
selectemp.send_keys('TESTING-DAVID')
selectemp.click()
time.sleep(1)
alt1 = Alert(driver)
alt1.accept()
time.sleep(1)
password = driver.find_element_by_xpath('//*[@id="form-password"]')
password.click()
password.send_keys('12345')
password.click()
time.sleep(1)
selectrole = driver.find_element_by_xpath('//*[@id="form-role"]')
selectrole.click()
selectrole.send_keys('Testing production-Intern')
selectrole.click()
time.sleep(1)
reportinto = driver.find_element_by_xpath('//*[@id="form-reporting_to"]')
reportinto.click()
reportinto.send_keys('Zeeshan Ahmad')
reportinto.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(5)
searchche = driver.find_element_by_xpath('//*[@id="form-user"]')
searchche.click()
searchche.send_keys('All')
searchche.click()
time.sleep(1)
find = driver.find_element_by_xpath('//*[@id="btn_search"]')
find.click()
time.sleep(1)
search = driver.find_element_by_xpath('//*[@id="manageAQMSTable_filter"]/label/input')
search.click()
search.send_keys('376')
time.sleep(1)
export = driver.find_element_by_xpath('//*[@id="btn_export"]')
export.click()
time.sleep(1)
logout = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/a')
logout.click()
time.sleep(1)
logoutt = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/ul/li[3]/a')
logoutt.click()
time.sleep(1)
form = driver.find_element_by_xpath('//form[@name="form"]')
username = form.find_element_by_xpath('//input[@id="username"]')
password = form.find_element_by_xpath('//input[@id="password"]')
username.send_keys("IAI001203")
password.send_keys("12345")
time.sleep(1)
login = form.find_element_by_xpath('//button[@type="submit"]')
login.click()
time.sleep(1)

sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
dash = driver.find_element_by_xpath('//*[@id="menulist"]/li[2]/a')
dash.click()
time.sleep(1)
brak = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[3]/button')
brak.click()
time.sleep(1)
short = driver.find_element_by_xpath('//*[@id="customRadio1"]')
short.click()
time.sleep(1)
long = driver.find_element_by_xpath('//*[@id="customRadio2"]')
long.click()
time.sleep(1)
full = driver.find_element_by_xpath('//*[@id="customRadio3"]')
full.click()
time.sleep(1)
emer = driver.find_element_by_xpath('//*[@id="customRadio4"]')
emer.click()
time.sleep(1)
can = driver.find_element_by_xpath('//*[@id="btn_close"]')
can.click()
i = 1
while i<=3:
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(2)
    i += 1
time.sleep(1)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
attendance = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
attendance.click()
time.sleep(1)
ar = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[1]/a')
ar.click()
time.sleep(1)
fromdate = driver.find_element_by_xpath('//*[@id="datepicker4"]')
fromdate.send_keys('02/22/2022')
time.sleep(1)
todate = driver.find_element_by_xpath('//*[@id="datepicker5"]')
todate.send_keys('03/01/2022')
time.sleep(1)
emp = driver.find_element_by_xpath('//*[@id="form-emp"]')
emp.click()
emp.send_keys('TESTING-DAVID')
emp.click()
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(1)
decending = driver.find_element_by_xpath('//*[@id="requesttbl"]/thead/tr/th[1]')
decending.click()
time.sleep(5)
search = driver.find_element_by_xpath('//*[@id="requesttbl_filter"]/label/input')
search.click()
search.send_keys('25')
time.sleep(1)
export = driver.find_element_by_xpath('//*[@id="exportreport"]')
export.click()
time.sleep(1)

sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
attendance = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
attendance.click()
time.sleep(1)
lm = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[2]/a')
lm.click()
time.sleep(1)
applyleave = driver.find_element_by_xpath('//*[@id="btn_add"]')
applyleave.click()
time.sleep(1)
formdate = driver.find_element_by_xpath('//*[@id="datefrom"]')
formdate.send_keys('03/01/2022')
time.sleep(1)
todate = driver.find_element_by_xpath('//*[@id="dateto"]')
todate.send_keys('03/05/2022')
time.sleep(1)
chosefile = driver.find_element_by_xpath('//*[@id="my_file"]')
chosefile.send_keys('D:\demo.txt')
time.sleep(1)
comnts = driver.find_element_by_xpath('//*[@id="cmttextare"]')
comnts.click()
comnts.send_keys('For testing purpose only')
time.sleep(1)
save = driver.find_element_by_xpath('//*[@id="submint_leave"]')
save.click()
time.sleep(1)
alt1 = Alert(driver)
alt1.accept()
time.sleep(1)
driver.execute_script("window.scrollBy(0,100)","")
time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="requesttbl_filter"]/label/input')
search.send_keys('03/01/2022')
time.sleep(1)
export = driver.find_element_by_xpath('//*[@id="btn_export"]')
export.click()
time.sleep(1)
home = driver.find_element_by_xpath('/html/body/div/div[1]/section[1]/ol/li[1]/a')
home.click()
time.sleep(1)
setting = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/a')
setting.click()
time.sleep(1)
logout = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/ul/li[3]/a')
logout.click()
time.sleep(1)

form = driver.find_element_by_xpath('//form[@name="form"]')
username = form.find_element_by_xpath('//input[@id="username"]')
password = form.find_element_by_xpath('//input[@id="password"]')
username.send_keys("IAI001055")
password.send_keys("12345")
time.sleep(1)
login = form.find_element_by_xpath('//button[@type="submit"]')
login.click()
time.sleep(3)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
AMS = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
AMS.click()
time.sleep(1)
lm = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[3]/a')
lm.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,100)","")
time.sleep(2)
driver.execute_script("window.scrollBy(0,100)","")
time.sleep(2)
reject = driver.find_element_by_xpath('//*[@id="3"]')
reject.click()
time.sleep(5)
sidebar = driver.find_element_by_xpath('//a[@class="sidebar-toggle"]')
sidebar.click()
clickon = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
clickon.click()
time.sleep(1)
sm = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[5]/a')
sm.click()
time.sleep(1)
manage = driver.find_element_by_xpath('//*[@id="employee_shift"]')
manage.click()
manage.send_keys(Keys.DOWN)
time.sleep(2)
manage.send_keys(Keys.DOWN)
time.sleep(2)
manage.send_keys(Keys.DOWN)
time.sleep(2)
manage.click()
time.sleep(1)
workinghour = driver.find_element_by_xpath('//*[@id="shift_from"]')
workinghour.send_keys('05:00')
workinghour.send_keys('PM')
time.sleep(1)
shifttime = driver.find_element_by_xpath('//*[@id="shift_to"]')
shifttime.send_keys('11:00')
shifttime.send_keys('AM')
shifttime.click()
time.sleep(1)
shiftdate  = driver.find_element_by_xpath('//*[@id="datepicker4"]')
shiftdate.send_keys('03/01/2022')
time.sleep(1)
comnts = driver.find_element_by_xpath('//*[@id="cmttextare"]')
comnts.click()
comnts.send_keys('qwertyhgdgvcdf')
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[3]/button[2]')
submit.click()
time.sleep(1)
alt1 = Alert(driver)
alt1.accept()
time.sleep(1)
formdate = driver.find_element_by_xpath('//*[@id="form-from"]')
formdate.click()
formdate.send_keys('02/20/2022')
time.sleep(1)
todate = driver.find_element_by_xpath('//*[@id="form-to"]')
todate.click()
todate.send_keys('03/02/2022')
time.sleep(1)
employee = driver.find_element_by_xpath('//*[@id="form-emp"]')
employee.click()
employee.send_keys(Keys.DOWN)
time.sleep(2)
employee.send_keys(Keys.DOWN)
time.sleep(2)
employee.send_keys(Keys.DOWN)
time.sleep(2)
employee.click()
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,800)","")
time.sleep(2)
setting = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/a')
setting.click()
time.sleep(1)
logout = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/ul/li[3]/a')
logout.click()
time.sleep(5)

form = driver.find_element_by_xpath('//form[@name="form"]')
username = form.find_element_by_xpath('//input[@id="username"]')
password = form.find_element_by_xpath('//input[@id="password"]')
username.send_keys("IAI001203")
password.send_keys("12345")
time.sleep(1)
login = form.find_element_by_xpath('//button[@type="submit"]')
login.click()
time.sleep(1)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
attendance = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
attendance.click()
time.sleep(1)
lm = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[2]/a')
lm.click()
time.sleep(1)
fordate = driver.find_element_by_xpath('//*[@id="form_from"]')
fordate.send_keys('02/20/2022')
time.sleep(1)
todate = driver.find_element_by_xpath('//*[@id="form_to"]')
todate.send_keys('03/05/2022')
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="requesttbl_filter"]/label/input')
search.click()
search.send_keys('2022-03-01')
time.sleep(1)
sidebar = driver.find_element_by_xpath('/html/body/div/header/nav/a')
sidebar.click()
time.sleep(1)
attendance = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/a')
attendance.click()
time.sleep(1)
sm = driver.find_element_by_xpath('//*[@id="menulist"]/li[3]/ul/li[3]/a')
sm.click()
time.sleep(1)
fordate = driver.find_element_by_xpath('//*[@id="form-from"]')
fordate.send_keys('03/01/2022')
time.sleep(1)
todate = driver.find_element_by_xpath('//*[@id="form-to"]')
todate.send_keys('03/05/2022')
time.sleep(1)
employee = driver.find_element_by_xpath('//*[@id="form-emp"]')
employee.click()
employee.send_keys('TESTING-DAVID')
time.sleep(1)
submit = driver.find_element_by_xpath('//*[@id="btn_submit"]')
submit.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="requesttbl_filter"]/label/input')
search.click()
search.send_keys('2022-03-01')
time.sleep(1)
home = driver.find_element_by_xpath('/html/body/div/div[1]/section[1]/ol/li[1]/a')
home.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(2)
brak = driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div[1]/div[1]/div[2]/div/div/div[1]/div[3]/button')
brak.click()
time.sleep(1)
short = driver.find_element_by_xpath('//*[@id="customRadio1"]')
short.click()
time.sleep(1)
long = driver.find_element_by_xpath('//*[@id="customRadio2"]')
long.click()
time.sleep(1)
full = driver.find_element_by_xpath('//*[@id="customRadio3"]')
full.click()
time.sleep(1)
emer = driver.find_element_by_xpath('//*[@id="customRadio4"]')
emer.click()
time.sleep(1)
can = driver.find_element_by_xpath('//*[@id="btn_close"]')
can.click()
time.sleep(1)
setting = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/a')
setting.click()
time.sleep(1)
logout = driver.find_element_by_xpath('/html/body/div/header/nav/div[1]/ul/li[2]/ul/li[3]/a')
logout.click()
time.sleep(5)
