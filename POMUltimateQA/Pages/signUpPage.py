from POMUltimateQA.Locators.locators import Locators
class SignUpPage():

    def __init__(self, driver):  # constructor
            self.driver = driver

            self.first_name_textbox_id = Locators.first_name_textbox_id
            self.last_name_textbox_id = Locators.last_name_textbox_id
            self.new_user_email_textbox_id = Locators.new_user_email_textbox_id
            self.new_user_password_textbox_id = Locators.new_user_password_textbox_id
            self.agreement_checkbox_id = Locators.agreement_checkbox_id
            self.privacy_linkText = Locators.privacy_linkText
            self.new_acc_sign_up_id = Locators.new_acc_sign_up_id

    def enter_user_first_name(self, userfirstname):
            self.driver.find_element_by_id(self.first_name_textbox_id).clear()
            self.driver.find_element_by_id(self.first_name_textbox_id).send_keys(userfirstname)

    def enter_user_last_name(self, userlastname):
            self.driver.find_element_by_id(self.last_name_textbox_id).clear()
            self.driver.find_element_by_id(self.last_name_textbox_id).send_keys(userlastname)

    def enter_new_user_email(self, newuseremail):
        self.driver.find_element_by_id(self.new_user_email_textbox_id).clear()
        self.driver.find_element_by_id(self.new_user_email_textbox_id).send_keys(newuseremail)

    def enter_new_user_password(self, password):
            self.driver.find_element_by_id(self.new_user_password_textbox_id).clear()
            self.driver.find_element_by_id(self.new_user_password_textbox_id).send_keys(password)

    def click_new_acc_sign_up(self):
            self.driver.find_element_by_id(self.new_acc_sign_up_id).click()
