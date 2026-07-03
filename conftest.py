import os

import outcome
import pytest
from config.settings import BASE_URL, BROWSER
from core.driver_factory import DriverFactory
from datetime import datetime

@pytest.fixture
def driver():

    """Creates and disposes the WebDriver instance."""

    driver = DriverFactory.get_driver(BROWSER)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(
    item,
    call):
    
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]
        
        timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
        )
        
        os.makedirs("screenshots", exist_ok=True)

        driver.save_screenshot(
        f"screenshots/{item.name}_{timestamp}.png"
        )