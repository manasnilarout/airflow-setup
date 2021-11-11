from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

def _model_A():
    return 9

def _choose_model_to_run(ti):
    acuuracies = ti.xcom_pull(task_id=['model_A', 'model_B', 'model_C'])
    best_accuracy = max(acuuracies)
    if (best_accuracy > 8):
        return 'accurate'
    return'inaccurate'

with DAG("dag-2", start_date=datetime(2021, 11, 11), schedule_interval="@daily", catchup=False) as dag:
    model_A = PythonOperator(
        task_id="model_A",
        python_callable=_model_A
    )

    model_B = PythonOperator(
        task_id="model_B",
        python_callable=_model_A
    )

    model_C = PythonOperator(
        task_id="model_C",
        python_callable=_model_A
    )

    choose_model = BranchPythonOperator(
        task_id="model_D",
        python_callable=_choose_model_to_run
    )

    accurate = BashOperator(
        task_id="model_E",
        bash_command="echo 'accurate"
    )

    inaccurate = BashOperator(
        task_id="model_F",
        bash_command="echo 'inaccurate"
    )

    [model_A, model_B, model_C] >> choose_model >> [accurate, inaccurate]