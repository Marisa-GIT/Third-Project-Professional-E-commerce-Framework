import os

import outcome
import pytest
from config.settings import BASE_URL, BROWSER
from core.driver_factory import DriverFactory
from datetime import datetime

@pytest.fixture
def driver():

    """Fixture to initialize and quit the WebDriver instance."""

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
        
        os.makedirs("screenshots", exist_ok=True)
        
        timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
        )
        
        driver.save_screenshot(
        f"screenshots/{timestamp}_{item.name}.png"
        )