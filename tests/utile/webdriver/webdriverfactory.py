from selenium import webdriver

class WebDriverFactory:
    __chrome_driver = lambda: webdriver.Chrome()
    __firefox_driver = lambda: webdriver.Firefox()
    __safari_driver = lambda: webdriver.Safari()

    map = {
        "chrome": __chrome_driver,
        "safari": __safari_driver,
        "firefox": __firefox_driver
    }

    @classmethod
    def get_driver(self, name):
        if name not in map:
            raise ValueError(f"Unsupported browser: {name}")
        return map[name]