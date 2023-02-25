# 手机端：要模拟的机型配置
WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

# 设定chrome的cookie
# 注意修改16569为你的用户名
profile_dir=r"C:\\Users\\16569\\AppData\\Local\\Google\\Chrome\\User Data"    # 对应你的chrome的用户数据存放路径 

# Chromedriver.exe的位置
chromedriver_path = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
