from selenium.webdriver.common.by import By


class HomePageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.profileButtonElement = "//img[@loading='eager']"
        self.settingsButtonElement = "//p[text()='Settings']"

    # Creating Element Methods
    def click_profile_button(self):
        profileButton = self.driver.find_element(By.XPATH, self.profileButtonElement)
        profileButton.click()


    def click_settings_button(self):
        settingsButton = self.driver.find_element(By.XPATH, self.settingsButtonElement)
        settingsButton.click()

