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

