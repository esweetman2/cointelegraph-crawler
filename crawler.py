import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options





def db_urls():
    # urls = []
    with open('urls.txt', 'r') as f:
        urls = f.readlines()  
    
    urls = [ i.replace('\n', "") for i in urls ]  
    return urls
    # print(urls)
# print(db_urls())


def get_urls():
    options = Options()
    options.headless = True
    driver  = webdriver.Chrome("C:\chromedriver.exe", options = options)
    driver.get("https://cointelegraph.com/tags/bitcoin")

    n=0
    urls = db_urls()
    while n < 100:
        print(n)
        try:
            load_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='__layout']/div/div[1]/main/div/div/div[4]/div/div/div/div/button"))
            )
            load_btn.send_keys(Keys.RETURN)
        except:
            print("couldn't click")
            break
        time.sleep(2)
        n+=1

    posts = driver.find_element_by_class_name('posts-listing__list')
    all_posts = posts.find_elements_by_tag_name("article")

    for post in all_posts:
        url = post.find_element_by_css_selector('a').get_attribute('href')
        with open("urls.txt", "a") as file1:
            # Writing data to a file
            if url in urls:
                n == 100
                print(f"{url} is on 'urls'")
                break
            else:
                file1.write(f"{url}\n")
get_urls()










