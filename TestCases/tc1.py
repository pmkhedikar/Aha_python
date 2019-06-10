from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

#driver =webdriver.Chrome()
driver: WebDriver = webdriver.Chrome(executable_path="D:\Aha_python\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://wwwqa.designmilktravels.com")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@class='mc-closeModal']").click()
driver.find_element_by_xpath("//*[@class='sign_in']").click()
driver.find_element_by_xpath("//*[@id='loginUsername']").send_keys('tuesday@dispostable.com')
driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys('pass@12345678')
driver.find_element_by_xpath("//*[@type='submit' and @value='Sign In']").click()
driver.find_element_by_xpath("//*[@class='account ']").click()
driver.close()