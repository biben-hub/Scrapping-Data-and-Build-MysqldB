import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class Database_Connection:
    
    def __init__(self):
        self.host     = 'localhost'
        self.user     = 'root2'
        self.password = 'rootroot'
        self.database = 'films_db'
        self.conex = mysql.connector.connect(self.host, self.user, self.password, self.database)
        self.my_cursor = self.conex.cursor()
 

    def create_db(self):
        self.my_cursor.execute('''CREATE DATABASE IF NOT EXISTS films_db CHARACTER SET utf8;''')
    
    def create_table(self):
                self.my_cursor.execute('''CREATE TABLE IF NOT EXISTS Films (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                                                            Name_movie VARCHAR(255) NOT NULL, 
                                                                            Date VARCHAR(255), 
                                                                            Time VARCHAR(20), 
                                                                            Category VARCHAR(100), 
                                                                            Productor VARCHAR(100), 
                                                                            Actors VARCHAR(255), 
                                                                            Picture VARCHAR(500),;''')


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