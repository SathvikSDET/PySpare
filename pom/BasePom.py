from abc import ABC,abstractmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePom(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)
        
    
    def find_element(self ,webelment):
        return self.wait.until(EC.presence_of_element_located(webelment))


    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config

    @abstractmethod
    def isElementDisplayed(self ,webelment):
        pass
