from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 1. 크롬 실행 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 창 최대화
chrome_options.add_experimental_option("detach", True)  # 창 자동 닫힘 방지

driver = webdriver.Chrome(options=chrome_options)
url = "https://www.musinsa.com/main/musinsa/ranking?gf=A&storeCode=musinsa&sectionId=200&contentsId=&categoryCode=000&ageBand=AGE_BAND_ALL"
driver.get(url)
time.sleep(2)

# 2. 스크롤 설정
scroll_step = 500         # 한 번에 내리는 픽셀 단위
interval = 1              # 스크롤 간격 (초)
max_scroll_time = 10      # 스크롤 시간 제한 (초)
start_time = time.time()

collected_titles = set()  # 중복 방지

# 3. 스크롤하면서 제목 실시간 추출
while True:
    # HTML 파싱
    soup = BeautifulSoup(driver.page_source, "lxml")
    posts = soup.find_all("div", attrs={"class":"pl-3 pr-2 pt-3 pb-6 bg-white UIProductColumn__InfoItem-sc-1t5ihy5-7 diMGVt"})

    # 제목 추출
    for post in posts:
        title_tag = post.find("p", attrs={"class":"text-body_13px_reg line-clamp-2 break-all whitespace-break-spaces text-black font-pretendard"})
        if title_tag:
            title = title_tag.get_text()
            if title not in collected_titles: # set에 없다면 해당 title 출력
                collected_titles.add(title)
 
                price = post.find("span", attrs={"class":"text-body_13px_semi UIProductColumn__PriceText-sc-1t5ihy5-11 cZhItm text-black font-pretendard"}).get_text() # 가격
                link = post.find("a", attrs={"class":"UIProductColumn__Anchor-sc-1t5ihy5-8 EyWwa gtm-select-item"})["href"] # 링크
                                  
                print(f"[{len(collected_titles)}] {title}")
                print(f"[가격: {price}")
                print(f"링크: {link}")

    # 스크롤 내리기
    driver.execute_script(f"window.scrollBy(0, {scroll_step});")
    time.sleep(interval)

    # 시간 초과 시 중단
    if time.time() - start_time > max_scroll_time:
        print("스크롤 시간 종료.")
        break

print("최종 수집된 상품 개수:", len(collected_titles))
print("수집 완료!")

# 브라우저 닫기
driver.quit()