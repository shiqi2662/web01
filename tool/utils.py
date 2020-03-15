from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import Base




class Utils:

    __driver = None

    @classmethod
    def get_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()

            cls.__driver.maximize_window()

        return cls.__driver

    @classmethod
    def quit_driver(cls):
        if cls.__driver is not None:

            cls.__driver.quit()
            cls.__driver = None

def exists_text(text):
    driver = Utils().get_driver()

    try:
        WebDriverWait(driver, 5, 0.5).until(lambda d: d.find_element(By.XPATH, "//*[text()='{}']".format(text)))
        return True

    except:
        return False



