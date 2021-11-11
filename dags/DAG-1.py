# DAG - 1
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'manas',
    'depends_on_past': False,
    'start_date': datetime(2021, 11, 10),
    'retries': 0
}

dag = DAG(dag_id='exp-1', default_args=default_args, catchup=False, schedule_interval='@once')

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end