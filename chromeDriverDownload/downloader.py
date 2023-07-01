import os
from selenium import webdriver
import chromedriver_autoinstaller

chrome_ver = chromedriver_autoinstaller.get_chrome_version()
print(chrome_ver)

chromedriver_autoinstaller.install(True)
chromedriver_path = "C:\chrome\chromedriver.exe"

webdriver.Chrome()