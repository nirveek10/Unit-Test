from selenium import webdriver
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_Nepal(self):
        self.driver.get("http://google.com")
        self.driver.find_element("name", "q").send_keys("Nepal's weather today")
        self.driver.find_element("name", "btnK").click()

    def test_search_Nep(self):
        self.driver.get("http://google.com")
        self.driver.find_element("name", "q").send_keys("Current time in Nepal")
        self.driver.find_element("name", "btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
