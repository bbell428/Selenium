# 무신사 웹사이트 동적부분때문에 가장 아래 스크롤은 웹 스크래핑 어려움.
# Shop_AutoScroll 해답

# 1. 무신사 사이트 열기
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

Options = Options()
Options.add_argument("--start-maximized") # 화면을 꽉 차게 띄우기
Options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=Options)
url = "https://www.musinsa.com/main/musinsa/ranking?gf=A&storeCode=musinsa&sectionId=200&contentsId=&categoryCode=000&ageBand=AGE_BAND_ALL"
browser.get(url)

interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height
print("스크롤 완료")

# 2. 최신 랭크 정보 가져오기
# Selenium으로 렌더링 후 HTML 가져오기
soup = BeautifulSoup(browser.page_source, "lxml")

# 포스트 카드 찾기
posts = soup.find_all("div", attrs={"class":"pl-3 pr-2 pt-3 pb-6 bg-white UIProductColumn__InfoItem-sc-1t5ihy5-7 diMGVt"})
print(f"총 포스트 개수: {len(posts)}")

for post in posts:
    title = post.find("p", attrs={"class":"text-body_13px_reg line-clamp-2 break-all whitespace-break-spaces text-black font-pretendard"}).get_text()
    print(title)

# with open("musinsa.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

# browser.quit()