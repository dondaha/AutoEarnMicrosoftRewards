import random
import time
import string
import os  
from selenium import webdriver
# 设定chrome的cookie
profile_dir=r"C:\\Users\\16569\\AppData\\Local\\Google\\Chrome\\User Data"    # 对应你的chrome的用户数据存放路径  
chrome_options=webdriver.ChromeOptions()  
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))

# 初始化桌面端browser
path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
browser1 = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
for i in range(1):
    random_str = ''.join(random.choices(string.ascii_letters, k=6))
    print(random_str)
    question = random_str
    url = f"https://cn.bing.com/search?q={question}"
    browser1.get(url)
    time.sleep(2)
