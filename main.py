
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time



url = f"https://pixabay.com/images/search/?order=ec&pagi=1"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# page = driver.find_element(By.CSS_SELECTOR,'').text
page = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > div:nth-child(5) > div'))).text
# print(page)
total_page = int(page.split(" ")[0].replace(",", ""))//100
print(total_page)
count = 1
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
new_height = 1000

while True:
    driver.execute_script(f"window.scrollTo(0, {new_height});")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = new_height + 1000
    if new_height>=last_height:
        break

classitem = driver.find_elements(By.CLASS_NAME,'photo-result-image')

for i in classitem:
    url = i.get_attribute('src')
    # print(url)
    if url.endswith('.jpg'):
        improve_url = url.replace("_360", "960_720")
        improve_url = improve_url.replace("_340", "960_720")
        print(improve_url)
        count = count + 1
        print(count)
# print(driver.find_element(By.XPATH, '//*[@id="paginator_clone"]/div').get_attribute('innerHTML'))
# WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[3]/div[2]/a'))).click()

# count = 1
for  i in range(2,total_page):
    url = f"https://pixabay.com/images/search/?order=ec&pagi={i}"
    driver.get(url)
    try:
        SCROLL_PAUSE_TIME = 2.5
        last_height = driver.execute_script("return document.body.scrollHeight")
        new_height = 1000

        while True:
            driver.execute_script(f"window.scrollTo(0, {new_height});")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = new_height + 1000
            if new_height>=last_height:
                break

        classitem = driver.find_elements(By.CLASS_NAME,'photo-result-image')

        for i in classitem:
            url = i.get_attribute('src')
            # print(url)
            if url.endswith('.jpg'):
                improve_url = url.replace("_360", "960_720")
                improve_url = improve_url.replace("_340", "960_720")
                print(improve_url)
                count = count + 1
                print(count)
        # print(driver.find_element(By.XPATH, '//*[@id="paginator_clone"]/div').get_attribute('innerHTML'))
        WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/a'))).click()
    
    except Exception as e:
        print(e)
        break



