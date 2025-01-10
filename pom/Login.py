from BasePom import BasePom
from selenium.webdriver.common.by import By
import time

class Login(BasePom):

    predefined_login = (By.XPATH , "//p[normalize-space()='Username : Admin']")
    predefined_password = (By.XPATH , "//p[normalize-space()='Password : admin123']")
    username = (By.XPATH,"//input[@placeholder='Username']")
    password = (By.XPATH,"//input[@placeholder='Password']")
    login_button = (By.XPATH,"//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username_value, password_value):
       
        username_element = self.find_element(self.username)
        password_element = self.find_element(self.password)
        login_button_element = self.find_element(self.login_button)
        
        
        username_element.send_keys(username_value)
        password_element.send_keys(password_value)
        login_button_element.click()

    def get_predefined_login(self):
       
        login_text = self.find_element(self.predefined_login).text
        password_text = self.find_element(self.predefined_password).text
        
        
        login = login_text.split(':')[1].strip()  
        password = password_text.split(':')[1].strip()  
        
        self.login(login, password)
    
    def isElementDisplayed(self, element_locator):
        element = self.find_element(element_locator)
        return element.is_displayed()


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()

    login_page = Login(driver)
    driver.set_page_load_timeout(20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  
    
    print("Testing predefined login...")
    login_page.get_predefined_login()

   
