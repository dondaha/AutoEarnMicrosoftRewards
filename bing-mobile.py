from selenium import webdriver
import os
import time
import random
import string

# 要模拟的机型
WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

# 设定chrome的cookie
profile_dir=r"C:\\Users\\16569\\AppData\\Local\\Google\\Chrome\\User Data"    # 对应你的chrome的用户数据存放路径  
chrome_options=webdriver.ChromeOptions()  
# 添加配置
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))
chrome_options.add_experimental_option("mobileEmulation", mobileEmulation)
 
# 启动配置好的浏览器
driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
                        #   ,options=options
                          ,chrome_options=chrome_options
                          )
 
for i in range(20):
    random_str = ''.join(random.choices(string.ascii_letters, k=6))
    print(random_str)
    question = random_str
    url = f"https://cn.bing.com/search?q={question}"
    driver.get(url)
    time.sleep(2)
driver.quit()
