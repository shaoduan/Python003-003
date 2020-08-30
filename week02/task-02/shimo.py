from selenium import webdriver
location = 'D:/apps/Mozilla Firefox/firefox.exe'
username = 'username'
password = 'password'
driver = webdriver.Firefox(firefox_binary=location)
driver.get('https://shimo.im')
print(driver.window_handles)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/nav/div[3]/a[2]/button').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
cookies = driver.get_cookies()
print(cookies)