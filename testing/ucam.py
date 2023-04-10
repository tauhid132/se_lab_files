from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost/se_api/testing/index.html")

# inp1 = driver.find_element('xpath', '//*[@id="CT1_St1"]')
# inp2 = driver.find_element('id','logMain_Password')
# submit = driver.find_element('id','logMain_Button1')

old_title = driver.title

# print(inp1.text)
# inp1.send_keys('username')
# inp2.send_keys('password')
# time.sleep(5)
# submit.click()

# new_title = driver.title

# checking values
inp1 = driver.find_element('xpath', '//*[@id="CT1_St1"]')
inp2 = driver.find_element('xpath', '//*[@id="CT2_St1"]')
inp3 = driver.find_element('xpath', '//*[@id="Mid_St1"]')
inp4 = driver.find_element('xpath', '//*[@id="Final_St1"]')

total = driver.find_element('xpath', '//*[@id="totalmarks_s1"]')

assumed_total = int(inp1.text) + int(inp2.text) + int(inp3.text) + int(inp4.text)

if ( int(total.text) == assumed_total):
	print("correct")
else:
	print("incorrect")


# if (int(inp1.text) == 10):
# 	print('correct')
# else:
# 	print('We are in!')

driver.quit()