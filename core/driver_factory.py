from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.browsers import Browsers
from config.settings import WINDOW_MAXIMIZED, DISABLE_NOTIFICATIONS

class DriverFactory:

    @staticmethod
    def get_driver(browser):
        
        drivers = {
            Browsers.CHROME: DriverFactory._create_chrome_driver,
            Browsers.FIREFOX: DriverFactory._create_firefox_driver,
            Browsers.EDGE: DriverFactory._create_edge_driver,
        }
        driver_creator = drivers.get(browser)

        if driver_creator is None:
            raise ValueError(f"Unsupported browser: {browser}")
        
        return driver_creator()
    
    @staticmethod
    def _configure_options(options):
        if WINDOW_MAXIMIZED:
            options.add_argument("--start-maximized")

        if DISABLE_NOTIFICATIONS:
            options.add_argument("--disable-notifications")

        return options
    
    @staticmethod
    def _create_chrome_driver():
        options = webdriver.ChromeOptions()

        options = DriverFactory._configure_options(options)

        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )
        return driver

    @staticmethod
    def _create_firefox_driver():
        
        options = webdriver.FirefoxOptions()

        options = DriverFactory._configure_options(options)

        driver = webdriver.firefox(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )
        return driver    
    
    @staticmethod
    def _create_edge_driver():
        
        options = webdriver.EdgeOptions()

        options = DriverFactory._configure_options(options)

        driver = webdriver.edge(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )
        return driver  