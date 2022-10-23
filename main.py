# coding:utf-8
import os
import time

from selenium import webdriver#导入库
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


if __name__ == "__main__":
    username = os.environ.get("USERNAME", None)
    password = os.environ.get("PASSWORD", None)

    #安装google核
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
    #driver = webdriver.Chrome()  # 声明浏览器

    #设定网址
    url_login = 'https://passport.ustc.edu.cn/login?service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin'
    url_user = 'https://weixine.ustc.edu.cn/2020/home'

    # 按钮登陆
    driver.get(url_login)  # 打开浏览器预设网址
    locator1 = (By.XPATH, '//*[@id="username"]')
    WebDriverWait(driver, 3, 0.3).until(EC.presence_of_element_located(locator1))
    driver.find_element(By.XPATH,'//*[@id="username"]').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    button_login = driver.find_element(By.XPATH,'//*[@id="login"]')
    button_login.click()

    #获取cookie
    cookie_get = driver.get_cookies()

    # 添加cookie
    driver.delete_all_cookies()
    time.sleep(5)
    driver.refresh()
    driver.get(url_user)
    cookies = cookie_get

    for cookie in cookies:
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    driver.refresh()

    driver.get(url_user)

    #签到
    locator2 = (By.XPATH, '//*[@id="report-submit-btn-a24"]')
    WebDriverWait(driver, 3, 0.3).until(EC.presence_of_element_located(locator2))
    button2 = driver.find_element(By.XPATH, '//*[@id="report-submit-btn-a24"]')
    button2.click()

    #关闭浏览器
    driver.close()
    driver.quit()
