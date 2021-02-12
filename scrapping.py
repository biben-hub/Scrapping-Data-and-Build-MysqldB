import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

nom_film         = []
date_sortie_film = []
duree_film       = []
categorie_film   = []
realisateur_film = []
acteurs_film     = []
note_film        = []
nationalite_film = []
image_film       = []
distributeur     = []

url  = "https://www.allocine.fr/films/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='meta-title-link')
nom_elements  = results.find_all_next('a', class_='meta-title-link')
date_elements = results.find_all_next('span', class_='date')
# duree_elements = results.find_all_next('a', class_='meta-title-link')
# categorie_elements = results.find_all_next('a', class_='meta-title-link')
# realisateur_elements = results.find_all_next('a', class_='meta-title-link')
# acteurs_elements = results.find_all_next('a', class_='meta-title-link')
# note_elements = results.find_all_next('a', class_='meta-title-link')
# nationalite_elements = results.find_all_next('a', class_='meta-title-link')
# image_elements = results.find_all_next('a', class_='meta-title-link')
# distributeur_elements = results.find_all_next('a', class_='meta-title-link')


for e in nom_elements:
    nom_film.append(e.text)
print(nom_film)

for e in date_elements:
    date_sortie_film.append(e.text)
print(date_sortie_film)


# try:
my_db = mysql.connector.connect(host     = 'localhost',
                                user     = 'root2',
                                password = 'rootroot',
                                database = 'films')

my_db.close()
    
# print(my_db)
#     if my_db.is_connected():
#         db_info = my_db.get_server_info()
#         print("Connected to MySQL Server version ", db_info)
#         cursor = my_db.cursor()

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (my_db.is_connected()):
#         my_db.close()
#         print("MySQL connection is closed")