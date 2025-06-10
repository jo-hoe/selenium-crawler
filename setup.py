from setuptools import setup, find_packages

setup(
    name="selenium-crawler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # list dependencies here
    ],
    author="Jo-Hoe",
    description="Creates a simple Selenium Webdriver, optimized for web scraping.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)