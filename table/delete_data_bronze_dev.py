from google.cloud import bigquery
from datetime import datetime, date
from dotenv import load_dotenv
import os

load_dotenv()

project_id = os.getenv('GCP_PROJECT_ID')
dataset_id = os.getenv('BQ_DATASET')
table_id = os.getenv('BQ_BRONZE_TABLE') 

current_date = date.today()

def delete_data_merge():
    client = bigquery.Client()
    try:
      query = f'''
    delete from `{project_id}.{dataset_id}.{table_id}` where book_date = '{current_date}'
    '''
      job = client.query(query)
      job.result()
      print(f'{current_date} data has been delete from bronze table')
    except Exception as e:
       print(str(e))