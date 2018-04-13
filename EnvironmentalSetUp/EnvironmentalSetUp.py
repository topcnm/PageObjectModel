from selenium import webdriver
import unittest
import sys


class EnvironmentalSetUp(unittest.TestCase):

    PLATFORM = 'MAC'
    BROWSER = 'firefox'

    @classmethod
    def setUpClass(cls):

        desired_caps = {
            'platform': cls.PLATFORM,
            'browserName': cls.BROWSER
        }

        # java - jar selenium - server - standalone - 3.11.0.jar - port 4444 - role hub

        # java -jar selenium-server-standalone-3.11.0.jar -role webdriver
        # -browser 'browserName=chrome, platform=MAC' -hubHost 127.0.0.1 -port 5555

        # java -jar selenium-server-standalone-3.11.0.jar -role webdriver
        # -browser 'browserName=firefox, platform=MAC' -hubHost 127.0.0.1 -port 6666

        # java -jar selenium-server-standalone-3.11.0.jar -role webdriver
        # -browser 'browserName=safari, platform=MAC' -hubHost 127.0.0.1 -port 7777

        base_url = "http://newtours.demoaut.com/mercurywelcome.php"
        # cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)
        cls.driver.implicitly_wait(5)
        cls.driver.get(base_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "main":
    if len(sys.argv) > 1:
        EnvironmentalSetUp.BROWSER = sys.argv.pop()
        EnvironmentalSetUp.PLATFORM = sys.argv.pop()
    unittest.main(verbosity=2)