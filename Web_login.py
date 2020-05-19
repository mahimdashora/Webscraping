from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://a.impartus.com/ilc/#/home")

loginID=driver.find_element_by_xpath('//*[@id="username"]')
password=driver.find_element_by_xpath('//*[@id="password"]')
loginID.send_keys('')#mail login
password.send_keys('')#my password
loginButton=driver.find_element_by_xpath('/html/body/ui-view/div/div/ui-view/div/div[1]/form/div[2]/div')
loginButton.click()
joinCS=driver.find_element_by_xpath('/html/body/div[1]/ui-view/div[1]/div[2]/ui-view/div/div[2]/div[3]/dashboard-interests/div/live-streaming-lectures/md-card/md-list/div[1]/div[1]/div[2]/button')

joinCS.click()

