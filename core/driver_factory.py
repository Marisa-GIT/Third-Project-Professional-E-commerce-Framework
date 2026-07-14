from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
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

        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            }
        )
        options.add_argument("--disable-features=PasswordLeakDetection")
        
        service = ChromeService()
        return webdriver.Chrome(
                service=service,
                options=options
            )

    @staticmethod
    def _create_firefox_driver():
        options = DriverFactory._configure_options(webdriver.FirefoxOptions())
        return webdriver.Firefox(options=options)
    
    @staticmethod
    def _create_edge_driver():
        options = DriverFactory._configure_options(webdriver.EdgeOptions())
        return webdriver.Edge(options=options)