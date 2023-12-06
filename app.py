# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests

url = 'https://www.foxsports.com/scores/nfl/'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
# print(doc.prettify())

teams = doc.find_all(string= 'SEA')

print(teams.parent)