from time import sleep 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CAREER_WEBSITE_URL = "https://www.collegedekho.com/careers/chemical-engineer"

class CareerScraper:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def test(self):
        self.browser.get(CAREER_WEBSITE_URL)
        sleep(10)

a = CareerScraper()
a.test()
