from sqlite3 import Cursor
import mysql.connector

def DatabaseCreate():
    cnx = mysql.connector.connect(user = 'root', password = 'hossein', host = 'localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Bank")
    Cursor.execute("")
    Cursor.close()
    cnx.close()

def TablesCreate():
    cnx = mysql.connector.connect(user = 'root', password = 'hossein', host = 'localhost', database = 'Bank')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Account(Accno INT(15) NOT NULL AUTO_INCREMENT,Name VARCHAR(25) NOT NULL, Age INT(5) NOT NULL, Occup VARCHAR(15) NOT NULL, Address VARCHAR(50) NOT NULL, Mob INT(11) NOT NULL, Aadharno INT(16), amt DOUBLE(20,5), AccType VARCHAR(15) NOT NULL, PRIMARY KEY (Accno))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS amt(Accno INT(15), Amtdeposite DOUBLE(20, 5), month VARCHAR(15) NOT NULL)")
    Cursor.close()
    cnx.close()



