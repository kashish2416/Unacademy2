from selenium.webdriver.common.by import By


class LandingPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.loginButtonElement = "//*[text()='Log in']"
        self.mobileNumberElement = "//input[@placeholder='Enter your mobile number']"
        self.secondLoginElement = "//button[@color='green' and @aria-label='Login']"
        self.verifyOtpElement = "//button[@color='green' and @aria-label='Verify OTP']"

    # Creating Element Methods
    def click_login_button(self):
        loginButton = self.driver.find_element(By.XPATH, self.loginButtonElement)
        loginButton.click()

    def enter_mobilenumber_textbox(self, mn):
        mobilenumberTextBox = self.driver.find_element(By.XPATH, self.mobileNumberElement)
        mobilenumberTextBox.click()
        mobilenumberTextBox.send_keys(mn)

    def click_secondlogin_button(self):
        secondloginButton = self.driver.find_element(By.XPATH, self.secondLoginElement)
        secondloginButton.click()

    def click_verifyOtp_button(self):
        verifyOtpButton = self.driver.find_element(By.XPATH, self.verifyOtpElement)
        verifyOtpButton.click()