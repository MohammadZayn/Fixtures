import pytest
from selenium.webdriver.common.by import By


class Test_Browsers:

    def test_logo(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.message = self.driver.find_element(By.XPATH, "//strong[normalize-space()='Welcome, please sign in!']").text
        try:
            self.driver.close()
            assert 'Welcome, please sign in!' in self.message
        except:
            assert "Mohammad" in self.message,"Sorry you have captured the wrong statement"

    def test_site(self,setup):
        self.driver = setup
        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        self.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@yourstore.com")
        self.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("admin")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
            self.driver.close()
            assert True
        except:
            self.driver.close()
            assert False, "Not logged in because you have passed the wrong email id and password"


