import pytest
from selene import browser


@pytest.fixture
def browser_window_config():
    browser.config.window_width = 1280
    browser.config.window_height = 720
