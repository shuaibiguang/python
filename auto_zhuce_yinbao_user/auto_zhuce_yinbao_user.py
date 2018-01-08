from selenium import webdriver
import xlrd,sys

hang = int(sys.argv[1])

print (hang)

data = xlrd.open_workbook("内蒙客户部署资料表(1).xlsx")

table = data.sheet_by_name('内蒙白总')

row_data = table.row_values(hang - 1)

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get("http://beta12.pospal.cn/account/register")
shop_name = driver.find_element_by_id('username')
shop_name.send_keys(row_data[4])

password = driver.find_element_by_id('password')
password.send_keys(row_data[5])

passwordRepeat = driver.find_element_by_id('passwordRepeat')
passwordRepeat.send_keys(row_data[5])

phone = driver.find_element_by_id('phone')
phone.send_keys('13824466163')

email = driver.find_element_by_id('email')
email.send_keys('vip@sunsult.com')

storename = driver.find_element_by_id('storename')
storename.send_keys(row_data[2])

addressDetail = driver.find_element_by_id('addressDetail')
addressDetail.send_keys(row_data[7])
