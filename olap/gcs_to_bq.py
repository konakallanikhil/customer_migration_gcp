from google.cloud import bigquery

# Function to load data from gcs to bigquery

def gcs_To_Bq(bucketname,foldername,filename,project_id,dataset_id,table_id):
  client = bigquery.Client()
  job_config = bigquery.LoadJobConfig(
    skip_leading_rows = 1,
    source_format = bigquery.SourceFormat.CSV
    )

  uri = f'gs://{bucketname}/{foldername}/{filename}'

  table = f'{project_id}.{dataset_id}.{table_id}'

  load_job = client.load_table_from_uri(
    uri,
    table,
    job_config = job_config
    )
  load_job.result()
  print('Data Successfully ingested into bigquery table')  