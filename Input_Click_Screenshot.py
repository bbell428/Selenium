from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# ----------------------------
# 화면이 꺼지는 현상을 방지
Options = Options()
Options.add_argument("--start-maximized")  # 화면을 꽉 차게 띄우기
Options.add_experimental_option("detach", True)  # 브라우저가 자동으로 닫히지 않게 하는 옵션
# ----------------------------

driver = webdriver.Chrome(options=Options)

url = "https://www.naver.com/"

driver.get(url)
time.sleep(3)  # 3초  딜레이

# 1
# query = driver.find_element(By.ID, "query")
# query.send_keys("테스트") # Input
# time.sleep(2)

# search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
# search_btn.click() # 클릭(액션)
# time.sleep(5)

# 2
driver.find_element(By.ID, "query").send_keys("테스트")  # Input
time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, "#search-btn").click() # 클릭(액션)
driver.find_element(By.ID, "query").send_keys(Keys.ENTER)  # 엔터키를 작동시킴
time.sleep(5)

driver.save_screenshot("naver_테스트.png")
driver.quit()  # 창 닫기
