'''
Title: Data Migration from legacy MYSQL to GCP
Person: Naga Venkata Nikhil Konakalla
Role: Data Engineer
Date: 15-07-2025 11:35:00
'''

from dbconn.connection import connection
from key.key import service_Key_Credentials
from oltp.sql_to_gcs import sql_To_Gcs
from dataset.customer_dataset_dev import create_bqdataset
from table.daily_customer_data_dev import create_bronze_table, project_id, dataset_id, table_id
from table.update_insert_data_dev import create_silver_table
from olap.gcs_to_bq import gcs_To_Bq
from merge.upsert_dev import up_sert_query
from table.delete_data_bronze_dev import delete_data_merge
import pandas as p
from datetime import date
from dotenv import load_dotenv
import os

try:
        # Here we are establishing the connection 
        connection = connection()

        # Current date
        current_date = date.today()

        # Here we are writing down the sql query for data extraction
        query = f'select * from customer where book_date = "{current_date}"'

        # Here we are creating the dataframe using read the data from sql query using python pandas
        df = p.read_sql(query, connection)

        # Here we are disconnecting the connection
        connection.close()

        # Here we are converting the data into csv format
        csv_file = 'data/customer.csv'
        df.to_csv(csv_file, index=False)

        #  Allowing the service key for access
        service_Key_Credentials()

        # Loading local file to gcs
        load_dotenv()
        bucketname = os.getenv('GCS_BUCKET')
        foldername = os.getenv('GCS_FOLDER')
        filename = f'customer_{current_date}.csv'
        sql_To_Gcs(bucketname,foldername,filename,csv_file)

        # Creating the dataset in bigquery
        create_bqdataset()

        # Create the table in bigquery
        create_bronze_table()

        # Tansfer the data GCS to bigquery table
        gcs_To_Bq(bucketname,foldername,filename,project_id,dataset_id,table_id)

        # Create the history table
        create_silver_table()

        # Here we write the upsert(update and insert) query
        up_sert_query()

        # Delete the existing data in table
        delete_data_merge()

except Exception as e:
        print('exception happend please check', str(e))