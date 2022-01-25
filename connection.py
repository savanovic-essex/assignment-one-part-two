#Import MySQL Connector module which allows for a connection with the databse
import mysql.connector


#Instantiate a connection with the database, by defining
#the host, the access credentials and the database name
connection = mysql.connector.connect( 
        host="localhost",
        user="root",
        passwd="codio",
        database="phonebook"
        )

#Instantiate cursor object in order to execute an SQL statement
cursor = connection.cursor()