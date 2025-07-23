from google.cloud import bigquery
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

project_id = os.getenv('GCP_PROJECT_ID')
dataset_id = os.getenv('BQ_DATASET')
target_table = os.getenv('BQ_SILVER_TABLE')
source_table = os.getenv('BQ_BRONZE_TABLE') 

def up_sert_query():
    client = bigquery.Client()
    query = f'''
    MERGE `{project_id}.{dataset_id}.{target_table}` AS target
    USING (             
    SELECT 
    SAFE_CAST(customer_id AS INT64) AS customer_id,
    customer_name,
    SAFE_CAST(age AS INT64) AS age,
    place,
    state,
    country,
    SAFE_CAST(mobile AS INT64) AS mobile,
    book_date
                            
    FROM `{project_id}.{dataset_id}.{source_table}`
    ) AS source
    ON target.customer_id = source.customer_id

    WHEN MATCHED THEN
    UPDATE SET
    target.customer_name = source.customer_name,
    target.age = source.age,
    target.place = source.place,
    target.state = source.state,
    target.country = source.country,
    target.mobile = source.mobile,
    target.book_date = source.book_date

    WHEN NOT MATCHED THEN
    INSERT (
    customer_id, customer_name, age, place, state, country, mobile, book_date
    )
    VALUES (
    source.customer_id,
    source.customer_name,
    source.age,
    source.place,
    source.state,
    source.country,
    source.mobile,
    source.book_date
    )
    '''
    job = client.query(query)
    job.result()
    print('Data has been succesfully merged into silver from bronze')

