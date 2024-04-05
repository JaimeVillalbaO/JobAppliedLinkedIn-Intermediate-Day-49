from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # keeps chrome open


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3823211693&f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&origin=JOB_SEARCH_PAGE_KEYWORD_AUTOCOMPLETE&refresh=true')

email = 'cryptobluewolf@gmail.com'
contrasena = os.environ.get('PASSWORD_CRYPTO')
sign_in = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
time.sleep(2)

username = driver.find_element(By.ID, value='username')
username.send_keys(email)

password = driver.find_element(By.ID, value='password')
password.send_keys(contrasena)

iniciar_sesion = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
iniciar_sesion.click()

time.sleep(5)

apply = driver.find_element(By.CSS_SELECTOR, value='.jobs-s-apply button')
apply.click()

cel = driver.find_element(By.ID, value='single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3823211693-111855866-phoneNumber-nationalNumber')
cel.send_keys('3216789392')

next = driver.find_element(By.CSS_SELECTOR, value='footer button')
next.click()

revew = driver.find_element(By.XPATH, value='//*[@id="ember248"]/span')
revew.click()