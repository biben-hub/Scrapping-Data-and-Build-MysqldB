import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# declaring variables to store the data we need
name_movie         = []
release_date_movie = []
length_movie       = []
category_film      = []
productor_movie    = []
actors_movie       = []
picture_movie      = []

# Load the webpage content
url  = "https://www.allocine.fr/films/"
page = requests.get(url)

# Convert to a beautiful soup object
soup = BeautifulSoup(page.content, 'html.parser')

# find the section with the data 
# section = soup.find('section', attrs = {'class', 'section section-wrap gd-3-cols gd-gap-20'})

movies = soup.find('li', class_= 'mdl')

name_elements = movies.find('h2', class_= 'meta-title').text.replace(' ', '')
print(name_elements)

date_time_cat_elements = movies.find('div', class_= 'meta-body-item meta-body-info').text.replace(' ', '').split()
for e in date_time_cat_elements:
    if e == '/':
        date_time_cat_elements.remove(e)
print(date_time_cat_elements)

production_elements = movies.find('a', class_='blue-link').text
print(production_elements)

actors_elements = movies.find('div', class_='meta-body-item meta-body-actor').text.replace(' ', '').split()
for e in actors_elements:
    if e == 'Avec':
        actors_elements.remove(e)
print(actors_elements)

picture_elements = movies.find





# my_db = mysql.connector.connect(host = 'localhost', user = 'root2', password = 'rootroot')

# cursor = my_db.cursor()

# cursor.execute("DROP DATABASE IF EXISTS films_db")
# print('droped')

# cursor.execute("CREATE DATABASE films_db")
# cursor.execute("SHOW DATABASES")

# for db in cursor:
#     print(db)

# cursor.execute("use {}".format(films_db))
# cursor.execute("CREATE TABLE film_list (id INT, name_movie VARCHAR(255))")
# print('created')

# query =  "ALTER TABLE film_list \ ADD name_movie VARCHAR(255) DEFAULT 'CS'"
# cursor.execute(query)
# # cursor.execute("DROP TABLE test")

# insert_sql = """INSERT INTO film_list (name_movie) VALUES (%s)"""
# val = [list([item]) for item in name_movie]
# cursor.executemany(insert_sql, val)
# my_db.commit()
# print("remains to insert", cursor.lastrowid)
# my_db.close()


