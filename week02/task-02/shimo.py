from selenium import webdriver
location = 'D:/apps/Mozilla Firefox/firefox.exe'
driver = webdriver.Firefox(firefox_binary=location)
driver.get('https://shimo.im')
d = driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/nav/div[3]/a[2]/button').click()
