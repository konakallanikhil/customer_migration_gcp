from google.cloud import bigquery
import os
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv('GCP_PROJECT_ID')
dataset_id = os.getenv('BQ_DATASET')
table_id = os.getenv('BQ_BRONZE_TABLE')

def create_bronze_table():
  client = bigquery.Client()
  table = f'{project_id}.{dataset_id}.{table_id}'
  try:
    client.get_table(table)
    print(f'{table} is already exist')
  except Exception as e:
    schema = [
      bigquery.SchemaField('customer_id','STRING'),
      bigquery.SchemaField('customer_name','STRING'),
      bigquery.SchemaField('age','STRING'),
      bigquery.SchemaField('place','STRING'),
      bigquery.SchemaField('state','STRING'),
      bigquery.SchemaField('country','STRING'),
      bigquery.SchemaField('mobile','STRING'),
      bigquery.SchemaField('book_date','STRING'),
    ]
    table = bigquery.Table(table, schema=schema)
    table = client.create_table(table)
    print(f'{table} has been created')