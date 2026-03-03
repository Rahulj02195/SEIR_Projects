import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
if len(sys.argv) < 2:
        print("Please enter an URL as well.")
        sys.exit()
url=sys.argv[1]
if "https://" not in url:
    url="https://"+url
def getPage(url): 
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.title
    body = driver.find_element(By.TAG_NAME, "body")
    links=driver.find_elements(By.TAG_NAME, "a")
    print("Title of the page: ", title)
    print("Body of the page: ")
    print(body.text)
    print("Links in the page: ")
    for link in links:
        href = link.get_attribute("href")
        if "https://" in href:
            print(href)
    driver.quit()
getPage(url)
