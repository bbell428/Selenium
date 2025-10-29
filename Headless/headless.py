from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# ----------------------------
options = Options()
# Options.headless = True # 옛날 방식
options.add_argument("--headless=new") # 최신 방식
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")  # 화면을 꽉 차게 띄우기
# ----------------------------

driver = webdriver.Chrome(options=options)

url = "https://www.naver.com/"
driver.get(url)

time.sleep(3)
driver.get_screenshot_as_file("naver.png")