import outcome
import pytest
from config.settings import BROWSER
from core.driver_factory import DriverFactory
from datetime import datetime

@pytest.fixture
def driver():

    driver = DriverFactory.get_driver(BROWSER)
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
        
        driver.save_screenshot(
        f"screenshots/{timestamp}.png"
        )