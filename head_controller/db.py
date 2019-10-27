import pymysql
import pymysql.cursors
import pandas as pd

def get_connection(db='NewDatabase'):

    databaseServerIP            = "127.0.0.1"  # IP address of the MySQL database server
    databaseUserName            = "root"       # User name of the database server
    databaseUserPassword        = ""           # Password for the database user
    newDatabaseName             = db # Name of the database that is to be created
    charSet                     = "utf8mb4"     # Character set
    cusrorType                  = pymysql.cursors.DictCursor
    connection   = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,
                                         charset=charSet,cursorclass=cusrorType,port=3306)
    return connection

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

def send_df_to_table(df,table_name):
    '''
    Sends a df to the sql server.
    Expects 'engine' variable to be set in parent function.
    '''

    try:
        connection
    except:
        raise Exception('connection must be set prior to running db.send_df_to_table().')
    assert df, 'df was emptry. Cannot send to db.'
    assert isinstance(df,pd.DataFrame()), 'Expected type DATAFRAME, but got type {}'.format(type(df))
    print('did nothing yet')
    return
