
from selenium import webdriver

from pom.Login import Login
from pom.SideBar.Sidebar import Sidebar

driver =webdriver.Chrome()
login = Login(driver)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  
login.get_predefined_login()

sidebar = Sidebar(driver)
sidebar.click()
sidebar.click_search("Admin")


