from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class infow():
    def __init__(self):
        self.driver=webdriver.Chrome()
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org/")
        time.sleep(2)
        search=self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        # time.sleep(10)
        search.send_keys(query)
        enter=self.driver.find_element(By.XPATH,'//*[@id="search-form"]/fieldset/button')
        enter.click()
        # time.sleep(100000)

# assist=infow()
# assist.get_info('dhruve rathi')


