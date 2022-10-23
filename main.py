# coding:utf-8
import os
from selenium import webdriver#导入库
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


if __name__ == "__main__":
    username = os.environ.get("USERNAME", None)
    password = os.environ.get("PASSWORD", None)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
    #browser = webdriver.Chrome()  # 声明浏览器
    url = 'https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin'
    browser.get(url)#打开浏览器预设网址
    locator1 = (By.XPATH, '//*[@id="username"]')
    WebDriverWait(browser, 3, 0.3).until(EC.presence_of_element_located(locator1))
    browser.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
    browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    button_login = browser.find_element(By.XPATH,'//*[@id="login"]')
    button_login.click()
    
    button2 = browser.find_element(By.XPATH, '//*[@id="report-submit-btn-a24"]')
    button2.click()
    browser.close()
    browser.quit()
