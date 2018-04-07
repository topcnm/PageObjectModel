from selenium.webdriver.common.by import By


class SeleniumWebDriver(object):

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_value):
        if locator_type == By.ID:
            return self.driver.find_element_by_id(locator_value)
        elif locator_type == By.NAME:
            return self.driver.find_element_by_name(locator_value)
        elif locator_type == By.LINK_TEXT:
            return self.driver.find_element_by_link_text(locator_value)
        elif locator_type == By.PARTIAL_LINK_TEXT:
            return self.driver.find_element_by_partial_link_text(locator_value)
        elif locator_type == By.TAG_NAME:
            return self.driver.find_element_by_tag_name(locator_value)
        elif locator_type == By.XPATH:
            return self.driver.find_element_by_xpath(locator_value)
        else:
            print("Locator type :" + locator_type + " is invalid or doesn't exit." )

