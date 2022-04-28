from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By


class RegistrationPage(StaticLiveServerTestCase):

    def setUp(self):
        self.service = ChromeService(
                        executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.wait = WebDriverWait(self.driver, 1000)

    def test_registration_page(self):

        self.driver.get(self.live_server_url + "/registration/")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_username"]'
                                 ).send_keys("TestFirstname")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_first_name"]'
                                 ).send_keys("TestFirstname")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_last_name"]'
                                 ).send_keys("TestLastname")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_email"]'
                                 ).send_keys("TestUser@mail.com")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_password1"]'
                                 ).send_keys("deigibefopn465")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="id_password2"]'
                                 ).send_keys("deigibefopn465")

        self.driver.find_element(By.XPATH,
                                 '//*[@id="registration-form"]/input[2]'
                                 ).click()
        self.wait.until(cond.url_changes)

        assert self.driver.current_url == self.live_server_url +\
            "/registration/login/"

    def tearDown(self):
        self.driver.close()
