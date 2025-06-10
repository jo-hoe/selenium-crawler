from typing import Union
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

MAX_WAIT_TIME_IN_SECONDS = 8


def get_clickable_element(element: Union[WebDriver, WebElement], mark: WebElement | tuple[str, str]) -> WebElement:
    element = WebDriverWait(element, MAX_WAIT_TIME_IN_SECONDS).until(
        EC.element_to_be_clickable(mark)
    )
    return element


def get_elements(element: Union[WebDriver, WebElement], locator: tuple[str, str], wait_time=MAX_WAIT_TIME_IN_SECONDS) -> list[WebElement]:
    WebDriverWait(element, wait_time).until(
        EC.presence_of_element_located(locator)
    )
    elements = element.find_elements(locator[0], locator[1])
    return elements


def get_element(element: Union[WebDriver, WebElement], locator: tuple[str, str], wait_time=MAX_WAIT_TIME_IN_SECONDS) -> WebElement:
    elements = get_elements(element, locator, wait_time)
    if not elements:
        raise ValueError(f"could not find element for xpath: {locator}")
    return elements[0]
