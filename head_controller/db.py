import pymysql
import pymysql.cursors
import pandas as pd
import sqlite3

import sqlite3
c = sqlite3.connect('data.db')
c.close()

def get_connection(db):
    DB = sqlite3.connect('data.db')
    return DB

def setup_db():
    try:
        # Create a cursor object
        con = db.get_connection()
        cursorInsatnce = con.cursor()
        # SQL Statement to create a database
        sqlStatement            = "CREATE DATABASE "+'head_controller'
        # Execute the create database SQL statment through the cursor instance
        cursorInsatnce.execute(sqlStatement)
        # SQL query string
        sqlQuery            = "USE head_controller"
        # Execute the sqlQuery
        cursorInsatnce.execute(sqlQuery)
        print('Successfully setup head_controller db.')
    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        con.close()



def send_df_to_table(df,table_name,operation='fail'):
    '''
    Sends a df to the sql server.
    Expects operation to be set to 'fail', 'append', or 'replace'.

    E.g. Usage:
    import db
    db.send_df_to_table(df,'test',operation='append')
    '''

    database = 'head_controller'

    assert len(df)!=0, 'df was empty. Cannot send to db.'

    try:
        # Create a cursor object
        con = get_connection(database)
        df.to_sql(name=table_name, con=con, if_exists = operation, index=False)

    except Exception as e:
        print("Exception occured:{}".format(e))

    finally:
        con.close()
    return
