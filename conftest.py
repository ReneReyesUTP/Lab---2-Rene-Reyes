import pytest
from selenium import webdriver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Obtener el fixture 'driver'
            driver = item.funcargs.get('driver', None)
            if driver:
                screenshot = driver.get_screenshot_as_base64()
                extra.append(pytest_html.extras.image(screenshot, 'Screenshot'))
        report.extra = extra
