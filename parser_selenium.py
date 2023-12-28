from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Configurate our webdriver
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--ignore-certificate-errors')
options.add_argument('log-level=3')

# Before using this path, you need to donwload webdriver from: https://googlechromelabs.github.io/chrome-for-testing/
service = webdriver.ChromeService(
    executable_path='./chromedriver-win64/chromedriver.exe')

# Create our webdriver
driver = webdriver.Chrome(service=service, options=options)

# Select currencies and amount to be converted (look at the list of currencies, which are supported by cash.rbc.ru)
from_currency = 'GBP'
to_currency = 'RUR'
sum = 1000

driver.get(f'''
https://cash.rbc.ru/converter.html?from={from_currency}&to={to_currency}&sum={sum}&date=&rate=cbrf
                   ''')

# Choose needed element
rate = driver.find_element(By.CLASS_NAME, "calc__input_box")
date = driver.find_element(By.CLASS_NAME, "calc__period")

# Format the information found
text = rate.text.split()
date_text = date.text.split()

# Close driver conection
driver.quit()

# Show the final result
print(f'Convert result:{sum} {from_currency} = {
      float(text[3])*sum} {to_currency}')
print(f'Information was taken from the official website of the Central Bank of Russia {
      date_text[2]} {date_text[3]}')
