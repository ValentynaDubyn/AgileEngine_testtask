from selenium import webdriver
import time
import unittest
import pytest
from POMUltimateQA.Pages.loginPage import LoginPage
from POMUltimateQA.Pages.forgotPasswordPage import ForgotPasswordPage

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

    def test_04_forgot_password(self):
        driver = self.driver

        driver.get("https://courses.ultimateqa.com/users/sign_in")
        driver.implicitly_wait(10)

        login = LoginPage(driver)
        passwordrecover = ForgotPasswordPage()
        login.click_forgot_password_link()
        passwordrecover.click_submit()
        time.sleep(2)

