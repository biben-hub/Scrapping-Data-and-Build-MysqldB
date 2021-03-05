import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

name_movie         = []
release_date_movie = []
length_movie       = []
category_film      = []
realisateur_movie  = []
actors_movie       = []
rate_movie         = []
language_movie     = []
picture_movie      = []
distribution_movie = []

url  = "https://www.allocine.fr/films/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='meta-title-link')
print(results)
name_elements  = results.find_all_next('a', class_='meta-title-link')
date_elements = results.find_all_next('span', class_='date')
# time_elements = results.find_all_next('a', class_='meta-title-link')
# categorie_elements = results.find_all_next('a', class_='meta-title-link')
# realisateur_elements = results.find_all_next('a', class_='meta-title-link')
# acteurs_elements = results.find_all_next('a', class_='meta-title-link')
# note_elements = results.find_all_next('a', class_='meta-title-link')
# nationalite_elements = results.find_all_next('a', class_='meta-title-link')
# image_elements = results.find_all_next('a', class_='meta-title-link')
# distributeur_elements = results.find_all_next('a', class_='meta-title-link')


for e in name_elements:
    name_movie.append(e.text)
print(name_movie)

for e in date_elements:
    release_date_movie.append(e.text)
print(release_date_movie)


my_db = mysql.connector.connect(host = 'localhost', 
                                user = 'root2',
                                password = 'rootroot')

cursor = my_db.cursor()

cursor.execute("DROP DATABASE IF EXISTS films_db")
print('droped')

cursor.execute("CREATE DATABASE films_db")
cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

# cursor.execute("use {}".format(films_db))
cursor.execute("CREATE TABLE film_list (id INT, name_movie VARCHAR(255))")
print('created')

# query =  "ALTER TABLE film_list \ ADD name_movie VARCHAR(255) DEFAULT 'CS'"
# cursor.execute(query)
# # cursor.execute("DROP TABLE test")

# insert_sql = """INSERT INTO film_list (name_movie) VALUES (%s)"""
# val = [list([item]) for item in name_movie]
# cursor.executemany(insert_sql, val)
# my_db.commit()
# print("remains to insert", cursor.lastrowid)
# my_db.close()


