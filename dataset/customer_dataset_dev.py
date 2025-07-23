import os
from dotenv import load_dotenv
from google.cloud import bigquery

load_dotenv()

project_id = os.getenv('GCP_PROJECT_ID')
dataset_id = os.getenv('BQ_DATASET')
env = os.getenv('ENVIRONMENT')

def create_bqdataset():
  print(f'This enviroment is for creating {env} datasets in bigquery')
  client = bigquery.Client(project = project_id)
  dataset = f'{project_id}.{dataset_id}'
  try:
    client.get_dataset(dataset)
    print(f'{dataset} is already exist')
  except Exception as e:
    dataset = bigquery.Dataset(dataset)
    dataset = client.create_dataset(dataset)
    print(f'{dataset} has been created')

