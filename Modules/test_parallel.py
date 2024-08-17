import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#  pytest -v -s -n=2 Modules/test_parallel.py -command to run the twi methods at a same time .N defines num of methods
#  to run
class TestLogin:
    Base_URL = "https://rahulshettyacademy.com/angularpractice/"

    def test_Booking(self, setup):
        import time

        # chrome driver - Chrome browser
        self.driver = setup
        self.driver.maximize_window()
        # Get the url of the page
        self.driver.get(self.Base_URL)
        # Click on the shop mode
        self.driver.find_element(By.XPATH, "//a[@href='/angularpractice/shop']").click()

        # get the common headers locator links
        self.products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        # Getting the titles of the products
        for x in self.products:
            title = x.find_element(By.XPATH, "div/h4/a").text
            if title == 'Blackberry':
                x.find_element(By.XPATH, "div/button").click()

        # Now checkout the cart
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

        # Searching for country
        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys('Ind')

        # Adding the explicit_wiat
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        # clicking the ind
        self.driver.find_element(By.LINK_TEXT, "India").click()

        # click the checkbox
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox.checkbox-primary").click()

        # Click on the purchase
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success.btn-lg").click()

        # Capturing the message
        message = self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text

        # Adding the condition
        assert "Success! Thank you!" in message

        # Adding  the screenshot
        self.driver.get_screenshot_as_file("sucess.png")

        self.driver.quit()


    def test_Verifying(self, setup):
        # chrome driver - Chrome browser
        self.driver = setup
        self.driver.maximize_window()

        # Get the Page url
        self.driver.get('https://rahulshettyacademy.com/loginpagePractise/')

        # Redirect the new link page
        self.driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

        # Now return the list of windows opened and pass the control to the new window page
        windows_opened = self.driver.window_handles
        self.driver.switch_to.window(windows_opened[1])
        capture = self.driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
        p_list = capture.split()
        print(p_list)

        # Now returns to the old window page
        self.driver.switch_to.window(windows_opened[0])

        # wait for few sec to load
        self.driver.implicitly_wait(5)

        # Enter the username and password
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(p_list[4])
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('ShammerSikandar')
        self.driver.find_element(By.CSS_SELECTOR, "label[for='terms']").click()

        # Click on the sign-in button
        self.driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))

        # Capture and display the message
        print(self.driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
        self.driver.quit()

