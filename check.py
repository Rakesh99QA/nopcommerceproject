from selenium import webdriver

import pytest

driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
driver.get("https://www.google.com/")
