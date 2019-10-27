import unittest
import Camera,db,Features
import pandas as pd
import pymysql
import db


class TestStringMethods(unittest.TestCase):

    #connection = db.get_connection()
    empty_df = pd.DataFrame()

    def test_create_connection(self):
        try:
            # Create a cursor object
            con = db.get_connection()
            cursorInsatnce = con.cursor()
            # SQL Statement to create a database
            sqlStatement            = "CREATE DATABASE "+'head_controller_'
            # Execute the create database SQL statment through the cursor instance
            cursorInsatnce.execute(sqlStatement)
            # SQL query string
            sqlQuery            = "SHOW DATABASES"
            # Execute the sqlQuery
            cursorInsatnce.execute(sqlQuery)

            #Fetch all the rows
            databaseList = cursorInsatnce.fetchall()
            for datatbase in databaseList:
                print(datatbase)

        except Exception as e:
            print("Exeception occured:{}".format(e))

        finally:
            con.close()

    def test_recal_connection(self):

        try:
            # Create a cursor object
            con = db.get_connection()
            cursorInsatnce = con.cursor()
            # SQL Statement to create a database
            sqlStatement            = "USE `head_controller`; SELECT * FROM head_controller"
            # Execute the create database SQL statment through the cursor instance
            cursorInsatnce.execute(sqlStatement)
            # SQL query string
            sqlQuery            = "SHOW DATABASES"
            # Execute the sqlQuery
            cursorInsatnce.execute(sqlQuery)

            #Fetch all the rows
            databaseList = cursorInsatnce.fetchall()
            for datatbase in databaseList:
                print(datatbase)

        except Exception as e:
            print("Exeception occured:{}".format(e))

        finally:
            con.close()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
