
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_path  = '/home/jiyeon/다운로드/chromedriver'
profile = "https://www.naver.com/"
nomad_coder = "https://nomadcoders.co/challenges"


# initialize browser to be controlled by Python

cService = webdriver.ChromeService()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = cService, options=options)
driver.implicitly_wait(5)
driver.get(nomad_coder)

login_button = driver.find_element(By.XPATH, '//*[@id="__next"]/header/nav/div[1]/div/div[3]/div/a')
login_button.click()
time.sleep(2)

email_ad = driver.find_element(By.ID, "email")
email_ad.send_keys("rlawldus3412@naver.com")
time.sleep(15)

checkbox=  driver.find_element(By.XPATH,'//*[@id="challenge-stage"]/div/label/input')
checkbox.click()
time.sleep(2)

continueBoc=  driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[1]/div/form/div[2]/span/button')
continueBoc.click()