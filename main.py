from time import sleep 
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

COLLEGEDEKHO_URL = "https://www.collegedekho.com" 


class CareerScraper:
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.refresh_page()

    def refresh_page(self):
        self.driver.get(COLLEGEDEKHO_URL + "/careers")

    def get_all_career_categories(self):
        """Returns a list of all the categories."""

        return self.driver.find_elements(By.CSS_SELECTOR, ".careerList > li")

    def get_all_career_links(self):
        """Returns list of all careers in a category"""

        return self.driver.find_elements(By.CSS_SELECTOR, '#ajax_block > div > div.container > ul > li > div > a')

def collect_data():
    career_scraper = CareerScraper()

    # {string: list} dictionary that maps category to list of links of careers in the category
    career_category_dict = {}
    categories = career_scraper.get_all_career_categories()

    for career_category in categories:
        career_category.click()
        sleep(1)

        # Get all a tags and initialize empty list for links
        career_a_tags = career_scraper.get_all_career_links()
        career_links = []

        # Extract link from a tag
        for a_tag in career_a_tags:
            url = a_tag.get_attribute("href")
            career_links.append(url)

        # Store list of links in career category dictionary 
        career_category_dict[career_category] = career_links

        # Click on the x
        career_scraper.driver.find_element(By.CSS_SELECTOR, "#ajax_block > div > div.container > div").click()


    print(career_category_dict)


collect_data()
