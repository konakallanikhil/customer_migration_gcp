'''
Tasks : 
1. Transfer the data to bronze to silver 
2. Update if the different content and if the record is new then insert the record

Packages according to requiremnt:
1. Airflow
2. os
3. BigqueryInsertJobOperator
4. Python Opertor
5. Empty Operator
6. Dummy Operator
7. BigqueryCreateEmptyDatasetOperator
8. BigqueryCreateEmptyTableOperator
9. TriggerDagRunOperator
10. up_stream
11. down_stream
12. XComm
13. gcsToBigqueryOperator
14. HookOperator
15. EmailOperator
15. GCSObjectExistenceSensor
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime,timedelta
import os
import sys

# Add path to locate main.py and other module files
sys.path.append('/path/to/your/project')

default_args = {
    'owner': 'Konkalla Naga Venkata Nikhil',
    'depends_on_past': False,
    'email_on_failure': True,
    # Optional: Add alerts
    'email': ['your_email@example.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'customer_data_migration',
    default_args=default_args,
    description='Daily migration from MySQL to BigQuery using GCS',
    # Daily at 9 AM IST
    schedule_interval='0 9 * * *',
    start_date=datetime(2025, 7, 21),
    catchup=False,
    tags=['ETL', 'MySQL', 'GCS', 'BigQuery']
)

def daily_Running_Dag():
    from main import run_main
    run_main()

start = EmptyOperator(
  task_id='Start',
  dag = dag
)

task = PythonOperator(
  task_id = 'Python Function calling',
  python_callable = daily_Running_Dag,
  dag = dag
)

end = EmptyOperator(
  task_id='End',
  dag = dag
)

start >> task >> end
