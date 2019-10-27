import pymysql
import pymysql.cursors
import pandas as pd

def get_connection():

    connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection

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
