import lxml
import requests
from bs4 import BeautifulSoup

# Choose currency pair to convert
values = 'eur-usd'

# Connect your values to website URL
url = f'https://ru.investing.com/currencies/{values}'

# Create a response
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
rates = soup.find_all(
    'span', class_='text-2xl')

# Format and get result
exchange_rate = rates[0].text.replace(',', '.')
print(float(exchange_rate))
