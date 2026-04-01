import os
import pytest
from playwright.sync_api import sync_playwright

from utils.config import Config


# Browser + Page Fixture
@pytest.fixture(scope="function")
def page(request):

    with sync_playwright() as p:

        if Config.BROWSER == "firefox":
            browser = p.firefox.launch(headless=Config.HEADLESS)
        elif Config.BROWSER == "webkit":
            browser = p.webkit.launch(headless=Config.HEADLESS)
        else:
            browser = p.chromium.launch(headless=Config.HEADLESS)

        context = browser.new_context()
        page = context.new_page()

        # Attach page to test for screenshots
        request.node.page = page

        yield page

        context.close()
        browser.close()

# Screenshot of failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = getattr(item, "page",None)

        if page:
            os.makedirs("screenshots", exist_ok=True)
            file_name = f"screenshots/{item.name}.png"
            page.screenshot(path=file_name)