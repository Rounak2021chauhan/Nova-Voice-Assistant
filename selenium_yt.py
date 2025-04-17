from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class music():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        time.sleep(2)
        video=self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        # time.sleep(100000)

# assist=music()
# assist.play('dhruve rathi')