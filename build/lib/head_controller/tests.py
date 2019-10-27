import unittest
import Camera,db,Features
import pandas as pd

# import the mysql client for python

import pymysql
# Create a connection object
databaseServerIP            = "127.0.0.1"  # IP address of the MySQL database server
databaseUserName            = "root"       # User name of the database server
databaseUserPassword        = ""           # Password for the database user
newDatabaseName             = "NewDatabase" # Name of the database that is to be created
charSet                     = "utf8mb4"     # Character set
cusrorType                  = pymysql.cursors.DictCursor
connectionInstance   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
                                     charset=charSet,cursorclass=cusrorType,port=3306)

try:
    # Create a cursor object
    cursorInsatnce        = connectionInstance.cursor()
    # SQL Statement to create a database
    sqlStatement            = "CREATE DATABASE "+newDatabaseName
    # Execute the create database SQL statment through the cursor instance
    cursorInsatnce.execute(sqlStatement)
    # SQL query string
    sqlQuery            = "SHOW DATABASES"
    # Execute the sqlQuery
    cursorInsatnce.execute(sqlQuery)

    #Fetch all the rows
    databaseList                = cursorInsatnce.fetchall()
    for datatbase in databaseList:
        print(datatbase)

except Exception as e:
    print("Exeception occured:{}".format(e))


finally:
    connectionInstance.close()

class TestStringMethods(unittest.TestCase):

    #connection = db.get_connection()
    empty_df = pd.DataFrame()

    # def test_db_connection(self):
    #     try:
    #         with connection.cursor() as cursor:
    #             # Create a new record
    #             sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #             cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    #         # connection is not autocommit by default. So you must commit to save
    #         # your changes.
    #         connection.commit()
    #
    #         with connection.cursor() as cursor:
    #             # Read a single record
    #             sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
    #             cursor.execute(sql, ('webmaster@python.org',))
    #             result = cursor.fetchone()
    #             print(result)
    #     finally:
    #         connection.close()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
