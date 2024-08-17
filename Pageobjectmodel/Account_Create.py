from selenium.webdriver.common.by import By


class New_Account:
    # Locators define
    texbox_FirstName_Id = "input-firstname"
    texbox_LastName_Id = "input-lastname"
    texbox_Email_Id = "input-email"
    texbox_Password_Id = "input-password"
    texbox_Agree_Xpath = "//input[@name='agree']"
    texbox_Continue_Xpath = "//button[@type='submit']"

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Action Methods:
    def firstname(self, firstname):
        firstnametxt = self.driver.find_element(By.ID,self.texbox_FirstName_Id)
        firstnametxt.clear()
        firstnametxt.send_keys(firstname)

    def lastname(self, lastname):
        lastnametxt = self.driver.find_element(By.ID, self.texbox_LastName_Id)
        lastnametxt.clear()
        lastnametxt.send_keys(lastname)

    def email(self, email):
        emailtxt = self.driver.find_element(By.ID, self.texbox_Email_Id)
        emailtxt.clear()
        emailtxt.send_keys(email)

    def password(self, password):
        passwordtxt = self.driver.find_element(By.ID, self.texbox_Password_Id)
        passwordtxt.clear()
        passwordtxt.send_keys(password)


    def agree(self):
        self.driver.find_element(By.XPATH, self.texbox_Agree_Xpath).click()

    def logon(self):
        self.driver.find_element(By.XPATH, self.texbox_Continue_Xpath).click()
