from time import sleep 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CAREER_WEBSITE_URL = "https://www.collegedekho.com/careers"

class CareerScraper:
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.refress_page()

    def refress_page(self):
        self.driver.get(CAREER_WEBSITE_URL)

    def get_all_career_categories(self):
        """Returns a list of all the categories."""

        return self.driver.find_elements(By.CSS_SELECTOR, ".careerList > li")

    def get_all_careers(self):
        """Returns list of all careers in a category"""
        self.driver.find_elements(By.CSS_SELECTOR, '#ajax_block > div > div.container > ul > li')

def collect_data():
    career_scraper = CareerScraper()
    categories = career_scraper.get_all_career_categories()
    for career_category in categories:
        career_category.click()
        sleep(2)
        career_scraper.driver.find_element(By.CSS_SELECTOR, "#ajax_block > div > div.container > div").click()


collect_data()
