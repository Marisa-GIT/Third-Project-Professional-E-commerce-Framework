from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
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

        driver = driver_creator()

        if WINDOW_MAXIMIZED:
            driver.maximize_window()

        return driver

    @staticmethod
    def _configure_chromium_options(options):
        if DISABLE_NOTIFICATIONS:
            options.add_argument("--disable-notifications")

        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )
        options.add_argument("--disable-features=PasswordLeakDetection")
        return options

    @staticmethod
    def _create_chrome_driver():
        options = DriverFactory._configure_chromium_options(
            webdriver.ChromeOptions()
        )
        return webdriver.Chrome(service=ChromeService(), options=options)

    @staticmethod
    def _create_firefox_driver():
        options = webdriver.FirefoxOptions()

        if DISABLE_NOTIFICATIONS:
            options.set_preference("dom.webnotifications.enabled", False)

        return webdriver.Firefox(service=FirefoxService(), options=options)

    @staticmethod
    def _create_edge_driver():
        options = DriverFactory._configure_chromium_options(
            webdriver.EdgeOptions()
        )
        return webdriver.Edge(service=EdgeService(), options=options)