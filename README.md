# Selenium Scraper

A simple, opinionated Selenium WebDriver setup optimized for web scraping with Chrome. Designed for quick, lightweight data extraction, especially in Dockerized environments.

## Features

- Chrome WebDriver configuration for scraping
- Headless mode and image loading control
- Optimizations for Docker, Windows, Linux, and MacOS
- Utilities for element selection and waiting
- Basic anti-bot detection tweaks

## Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/jo-hoe/selenium-crawler.git
   cd selenium-crawler
   ```

2. Create a virtual environment and install dependencies:

   ```sh
   make init
   ```

   Or manually:

   ```sh
   python -m venv .venv
   .venv/Scripts/pip install -r requirements.txt
   ```

## Usage

Import and use the WebDriver creator and scraping tools in your scripts:

```python
from selenium_crawler.webdrivercreator import create_webdriver
from selenium_crawler.scraping_tools import get_element
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = create_webdriver(headless=True)
try:
    driver.get('https://example.com')
    element = get_element(driver, (By.XPATH, '//h1'), timeout=10)
    print(element.text)
except TimeoutException:
    print('Element not found within the timeout period.')
finally:
    driver.quit()
```

## Testing

Run all tests with:

```sh
make test
```

Or manually:

```sh
python -m unittest discover -s tests -v
```

## Notes

- This project is not intended to bypass all bot detection mechanisms.
- Focuses on ease of use and quick setup for scraping tasks.
- For advanced anti-bot evasion, consider additional tools or services.

## License

MIT License
