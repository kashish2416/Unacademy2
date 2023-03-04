from behave import *
import time
from features.pages.LandingPageClass import LandingPageClass
from features.pages.HomePageClass import HomePageClass
from features.pages.SettingsPageClass import SettingsPageClass

from datafiles import ExcelUtils
from features.utility.ConfigClass import ConfigClass



@step("User sends {invalid} data")
def step_impl(context,invalid):
    time.sleep(5)
    ExcelUtils.get_row_count(ConfigClass.datafilepath, "Sheet1")
    invalid = ExcelUtils.read_data(ConfigClass.datafilepath, "Sheet1", 2,1)
    Settings = SettingsPageClass(context.driver)
    Settings.enter_invusername_textbox(invalid)


@then("It shows result in page1")
def step_impl(context):
    expectedURL = "https://unacademy.com/settings"
    pageURL = context.driver.current_url

    try:
        time.sleep(5)
        if (expectedURL == pageURL):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.datafilepath, "Sheet1", 2, 2, "Failed")
            assert False
    finally:
        time.sleep(4)
        print(pageURL)




