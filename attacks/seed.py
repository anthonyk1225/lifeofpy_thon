import requests
from bs4 import BeautifulSoup
from attacks.models import Attack

r = requests.get('http://pokemondb.net/move/all')
soup = BeautifulSoup(r.text)
[for row in soup.table.tbody]