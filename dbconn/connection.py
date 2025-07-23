import mysql.connector

# Basically we are stablishing the connection of SQL Server to extract the data 

'''
Here the required data for establishing the connection
1. Host
2. User
3. Password
4. Database
'''

def connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='gcpproject'
    )
    return connection
