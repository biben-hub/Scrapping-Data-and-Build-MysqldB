import requests
from bs4 import BeautifulSoup

nom_film         = []
date_sortie_film = []
durée_film       = []
catégorie_film   = []
réalisateur_film = []
acteurs_film     = []
note_film        = []
nationalité_film = []
image_film       = []
distributeur     = []

url  = "https://www.allocine.fr/films/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
results = soup.find_all(id="")