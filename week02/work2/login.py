from selenium import webdriver
import time
url="https://shimo.im/welcome"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(10)
login=driver.find_element_by_xpath("//button[text()='登录']")
login.click()
name=driver.find_element_by_xpath("//input[@name='mobileOrEmail']")
name.send_keys("18911734601")
password=driver.find_element_by_xpath("//input[@name='password']")
password.send_keys("shimo123")
button=driver.find_element_by_xpath("//button[text()='立即登录']")
button.click()
time.sleep(1)
after_url="https://shimo.im/dashboard/used"
print(driver.current_url)
if driver.current_url==after_url:
    print("登录成功！")
time.sleep(3)
driver.quit()