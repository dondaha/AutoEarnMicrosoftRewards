import random
import time
import string
import os  
from selenium import webdriver
from config import mobileEmulation, profile_dir, chromedriver_path

# 配置Chrome
chrome_options=webdriver.ChromeOptions()  
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))

# 启动配置好的浏览器
driver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options)
for i in range(30):
    random_str = ''.join(random.choices(string.ascii_letters, k=6))
    print(random_str)
    question = random_str
    url = f"https://cn.bing.com/search?q={question}"
    driver.get(url)
    time.sleep(2)
driver.quit()
