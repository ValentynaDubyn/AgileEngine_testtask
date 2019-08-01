from selenium import webdriver
import time
import unittest
import pytest
from POMUltimateQA.Pages.loginPage import LoginPage
from POMUltimateQA.Pages.signUpPage import SignUpPage

class TestAccCreation(unittest.TestCase):
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = self.webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        yield
        driver.close()
        driver.quit()
        print("The test is completed")

    def test_05_acc_creation(test_setup):
        driver = test_setup.driver

        driver.get("https://courses.ultimateqa.com/users/sign_in")
        driver.implicitly_wait(10)

        login = LoginPage(driver)
        signup = SignUpPage(driver)
        login.click_new_acc_link()
        signup.enter_user_first_name("test")
        time.sleep(2)



