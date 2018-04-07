from selenium import webdriver
import unittest


class EnvironmentalSetUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_url = "http://newtours.demoaut.com/mercurywelcome.php"
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.get(base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    unittest.main(verbosity=2)