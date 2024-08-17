from selenium import webdriver
from Account_Create import New_Account
from webdriver_manager.chrome import ChromeDriverManager


# noinspection PyTypeChecker
class Test_Login:


    def test_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        self.driver.maximize_window()

        self.nw = New_Account(self.driver)
        self.nw.firstname("Mohammad")
        self.nw.lastname('Shaikh')
        self.nw.email("Mohammadshaik776@gmail.com")
        self.nw.password('Mohammad47@')
        self.nw.agree()
        self.nw.logon()


 