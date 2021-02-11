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
results = soup.find(class_='meta-title-link')
elements = results.find_all_next('a', class_='meta-title-link')
for e in elements:
    print(e.text, end='\n')

