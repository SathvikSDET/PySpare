
from pom.BasePom import BasePom
from selenium.webdriver.common.by import By

class Topbar(BasePom):
    """
    Topbar class for OrangeHRM
    """
    topbar_name = (By.CSS_SELECTOR,"span[class*='oxd-topbar-header-breadcrumb']")
    topbar_user_name = (By.CSS_SELECTOR,"p[class='oxd-userdropdown-name']")
    topbar_dropdown_name = (By.CSS_SELECTOR,"i[class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    topbar_logout = (By.CSS_SELECTOR,"a[class*='oxd-userdropdown-link'][href='/web/index.php/auth/logout']")
   
   
    def click_logout(self):
        self.find_element(self.topbar_dropdown_name).click()
        self.find_element(self.topbar_logout).click()
    def __init__(self, driver):
        super().__init__(driver)
    def get_topbar_name(self):
        return self.find_element(self.topbar_name).text
    def get_topbar_name(self):
        return self.find_element(self.topbar_user_name).text
