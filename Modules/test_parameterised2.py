import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Test_Paramerised:

    @pytest.mark.parametrize("user,pwd", [("Admin", 'admin123'),
                                          ("Admin", "Ya123"),
                                          ('admin', "sara123"),
                                          ("sara", "enchilada123")])
    def test_LoginSuccessful(self, user, pwd,setup):
        self.driver = setup
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys(user)
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']").send_keys(pwd)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        try:
            self.status = self.driver.find_element(By.XPATH, "(//h6[normalize-space()='Dashboard'])[1]").is_displayed()
            self.driver.close()
            assert self.status == True
        except:
            self.driver.close()
            assert False
