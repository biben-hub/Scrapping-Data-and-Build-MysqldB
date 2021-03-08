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
movies = soup.find('li', class_= 'mdl')



# fetching all the data
name_elements = movies.find('h2', class_= 'meta-title').text
print(name_elements)

date_time_cat_elements = movies.find('div', class_= 'meta-body-item meta-body-info').text.replace(' ', '').split()
for e in date_time_cat_elements:
    if e == '/':
        date_time_cat_elements.remove(e)
print(date_time_cat_elements)

production_elements = movies.find('a', class_= 'blue-link').text
print(production_elements)

actors_elements = movies.find('div', class_= 'meta-body-item meta-body-actor').text.replace(' ', '').split()
for e in actors_elements:
    if e == 'Avec':
        actors_elements.remove(e)
print(actors_elements)

picture_elements = movies.find('img', class_= 'thumbnail-img')
print(picture_elements["src"])








