from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost/011201166/testE/index.html")

salary = driver.find_element('xpath', '//*[@id="f0"]')
extra_salary = driver.find_element('xpath', '//*[@id="f1"]')
submit = driver.find_element('xpath', '/html/body/form/p[2]/input')
salary.send_keys('15000')
extra_salary.send_keys('12000')
time.sleep(3)
submit.click()
time.sleep(3)
driver.get(driver.current_url)
time.sleep(2)
result = driver.find_element('xpath', '//*[@id="s"]')

high_claim = 15000 + min(15000, (15000*.50)) + (15000*.5)
if int(result.text) <= int(high_claim):
	print('Test Case #1 OK')
else:
	print('Test Case #1 Wrong')
time.sleep(2)
driver.get("http://localhost/011201166/testE/index.html")

salary = driver.find_element('xpath', '//*[@id="f0"]')
extra_salary = driver.find_element('xpath', '//*[@id="f1"]')
submit = driver.find_element('xpath', '/html/body/form/p[2]/input')
salary.send_keys('50000')
extra_salary.send_keys('25000')
time.sleep(3)
submit.click()
time.sleep(3)
driver.get(driver.current_url)
time.sleep(2)
result = driver.find_element('xpath', '//*[@id="s"]')

high_claim = 25000 + min(15000, (50000*.50)) + (25000*.5)
if int(result.text) <= int(high_claim):
	print('Test Case #2 OK')
else:
	print('Test Case #2 Wrong')

time.sleep(2)
driver.get("http://localhost/011201166/testE/index.html")

salary = driver.find_element('xpath', '//*[@id="f0"]')
extra_salary = driver.find_element('xpath', '//*[@id="f1"]')
submit = driver.find_element('xpath', '/html/body/form/p[2]/input')
salary.send_keys('50000')
extra_salary.send_keys('25000')
time.sleep(3)
submit.click()
time.sleep(3)
driver.get(driver.current_url)
time.sleep(2)
result = driver.find_element('xpath', '//*[@id="s"]')

high_claim = 50000 + min(15000, (50000*.50)) + (50000*.5)
if int(result.text) <= int(high_claim):
	print('Test Case #3 OK')
else:
	print('Test Case #3 Wrong')

time.sleep(2)
driver.get("http://localhost/011201166/testE/index.html")

salary = driver.find_element('xpath', '//*[@id="f0"]')
extra_salary = driver.find_element('xpath', '//*[@id="f1"]')
submit = driver.find_element('xpath', '/html/body/form/p[2]/input')
salary.send_keys('15000')
extra_salary.send_keys('7000')
time.sleep(3)
submit.click()
time.sleep(3)
driver.get(driver.current_url)
time.sleep(2)
result = driver.find_element('xpath', '//*[@id="s"]')

high_claim = 15000 + min(15000, (15000*.50)) + (15000*.5)
if int(result.text) <= int(high_claim):
	print('Test Case #4 OK')
else:
	print('Test Case #4 Wrong')

time.sleep(2)
driver.get("http://localhost/011201166/testE/index.html")

salary = driver.find_element('xpath', '//*[@id="f0"]')
extra_salary = driver.find_element('xpath', '//*[@id="f1"]')
submit = driver.find_element('xpath', '/html/body/form/p[2]/input')
salary.send_keys('12500')
extra_salary.send_keys('11000')
time.sleep(3)
submit.click()
time.sleep(3)
driver.get(driver.current_url)
time.sleep(2)
result = driver.find_element('xpath', '//*[@id="s"]')

high_claim = 12500 + min(15000, (12500*.50)) + (12500*.5)
if int(result.text) <= int(high_claim):
	print('Test Case #5 OK')
else:
	print('Test Case #5 Wrong')
driver.quit()