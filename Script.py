from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AS5LTASbB0xOJv39OPT-wQnl3Ua0edTTYzerQxsM-R_1qwgIl0JVJr2vCezWWKbuT0wleLPqCfZlUg&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1510740936%3A1719231819942363&ddm=0")

email = driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]')
next1 = driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button')
email.send_keys("mariammazen988@gmail.com")
driver.implicitly_wait(0.5)
next1.click()
driver.implicitly_wait(10)

password = driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
next2 = driver.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button')
password.send_keys("Mariam123")
driver.implicitly_wait(0.5)
next2.click()
driver.implicitly_wait(10)
search_box = driver.find_element(by=By.XPATH, value='//*[@id="gs_lc50"]/input[1]')
search_button = driver.find_element(by=By.XPATH, value='//*[@id="aso_search_form_anchor"]/button[4]')
search_box.send_keys("subject:Searchbythis")
search_button.click()
driver.implicitly_wait(10000)

driver.find_element(by=By.XPATH, value='//*[@id=":50"]').click()
driver.implicitly_wait(100000)

