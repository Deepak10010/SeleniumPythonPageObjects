from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


from Utilities import configReader
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).click()


    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.readConfig("locators", locator)).send_keys(value)



    def select(self, locator, value):
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        select = Select(dropdown)
        select.select_by_visible_text(value)



    def moveTo(self, locator):
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.readConfig("locators", locator))

        action = ActionChains(self.driver)
        action.move_to_element(element).perform()


