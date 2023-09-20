from selene.support.shared import browser
from selene import be, have


def test_result_is_found(browser_window_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_result_not_found(browser_window_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('homework3_notfounderror_terytgue').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу  ничего не найдено. '))
