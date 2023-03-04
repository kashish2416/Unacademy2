from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SettingsPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.editStateButtonElement = "//button[@aria-label='Edit State' and @color='green']"
        #self.chooseStateElemet = "//span[text()='Maharashtra']"
        self.saveButtonElement = "//button[@aria-label='Save']"
        self.editEmailButtonElement = "//button[@aria-label='Edit email' and @color='green']"
        self.editEmailTextboxElement = "//input[@placeholder='Email' and aria-invalid name='email']"
        self.editUsernameButtonElement = "//button[@aria-label='Edit username']"
        self.editUsernameTextboxElement = "//input[@placeholder='Username']"
        self.editinvUsernameTextboxElement = "//input[@placeholder='Username']"
        self.usaveButtonElement = "//button[@aria-label='Save']"

    # Creating Element Methods
    def click_editstate_buttonelement(self):
        elements = self.driver.find_element(By.XPATH, self.editStateButtonElement)
        elements.send_keys(Keys.ENTER)


    def click_save_button(self):
        saveButton = self.driver.find_element(By.XPATH, self.saveButtonElement)
        saveButton.click()

    def click_editEmail_button(self):

        editemail = self.driver.find_element(By.XPATH, self.editEmailButtonElement)
        editemail.send_keys(Keys.ENTER)

    def enter_email_textbox(self, em):
        emailText = self.driver.find_element(By.XPATH, self.editEmailTextboxElement)
        emailText.clear()
        emailText.send_keys(em)

    def refresh_button(self):
        self.driver.refresh()

    def click_edit_username_button(self):
        unamebutton = self.driver.find_element(By.XPATH, self.editUsernameButtonElement)
        unamebutton.send_keys(Keys.ENTER)


    def enter_username_textbox(self,uname):
        unameTextbox = self.driver.find_element(By.XPATH, self.editUsernameTextboxElement)
        unameTextbox.send_keys(uname)

    def enter_invusername_textbox(self,invuname):
        invunameTextbox = self.driver.find_element(By.XPATH, self.editinvUsernameTextboxElement)
        invunameTextbox.send_keys(invuname)

    def click_usave_button(self):
        usaveButton = self.driver.find_element(By.XPATH, self.usaveButtonElement)
        usaveButton.click()
