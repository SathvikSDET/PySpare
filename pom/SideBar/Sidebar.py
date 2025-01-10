
from ..BasePom import BasePom

from selenium.webdriver.common.by import By
from pom.Login import Login

class Sidebar(BasePom):

    element = (By.XPATH , "//i[@class='oxd-icon bi-chevron-right']")
    sidebar_search = (By.XPATH , "//input[@placeholder='Search']")
    seach_list = (By.XPATH , "//ul[@class='oxd-main-menu']")
    def __init__(self,driver):
        super().__init__(driver)

    def isElementDisplayed(self, element):
        return self.find_element(element).is_displayed()

    def click(self):
        locator = self.find_element(self.element)
        locator.click()
    
    def click_search(self,word):
        seacrh = self.find_element(self.sidebar_search);
        seacrh.clear()  
        seacrh.send_keys(word)

    def get_elements_after_click(self):
        slist = self.find_elements(self.seach_list)
        return slist
    
    def click_search_list(self,word):
        slist = self.get_elements_after_click()
        for s in slist:
            if s.text == word:
                s.click()
                break

if __name__ == '__main__':
 
    driver = webdriver.Chrome()

    login_page = Login(driver)
    driver.set_page_load_timeout(20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  
    
    login_page.get_predefined_login()




