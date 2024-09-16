from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from info import chrome_driver_path

def extract_instagram_posts(username, password, search_query):

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    post_urls = []

    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)

        # Log in
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get(f"https://www.instagram.com/explore/tags/{search_query[1:]}/")
        time.sleep(5)

        posts = driver.find_elements(By.CSS_SELECTOR, "article a")
        for post in posts:
            post_url = post.get_attribute('href')
            post_urls.append(post_url)
    
    finally:
        driver.quit()

    return post_urls