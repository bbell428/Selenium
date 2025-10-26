from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("User Agent")

browser = webdriver.Chrome(options=options)

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
# AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/84.0.4147.89 Safari/537.36
detected_value = browser.find_element_by_id("")
print(detected_value.text)
browser.quit()