from selenium import webdriver
from selenium.webdriver.common.by import By
import time

User_name = "Your Mail Id"
Pass = "Your Password"

selenium_dir = r"Selenium directory"
driver = webdriver.Chrome(executable_path=selenium_dir)
driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')
time.sleep(5)
the_result3 = driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
the_result3.click()
time.sleep(5)
the_result = driver.find_element(By.NAME, "session_key")
the_result.send_keys(User_name)
the_result1 = driver.find_element(By.NAME, "session_password")
the_result1.send_keys(Pass)
the_result2 =driver.find_element(By.XPATH,'/html/body/div/main/div[2]/div[1]/form/div[3]/button')
the_result2.click()
time.sleep(5)
the_result4 = driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button/span')
the_result4.click()
time.sleep(5)
the_result5 = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/form/div/div[1]/div[4]/div/div/div[1]/div/input')
the_result5.send_keys("Your Phone No")
the_result6 = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/form/div/div[2]/div/div[1]/div/div[2]/div/div[2]/button[1]/span')
the_result6.click()
the_result7 = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/form/footer/div[3]/button/span')
the_result7.click()
time.sleep(10)
print("Application submitted")
driver.close()
