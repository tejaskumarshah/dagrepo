from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 2, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'tejas_daily_bash_dag',
    default_args=default_args,
    description='A simple bash command example running daily at 11 PM',
    schedule_interval='0 23 * * *',  # 11 PM daily
    catchup=False,
) as dag:

    bash_command = 'echo "Hello, Airflow! Daily run at 11 PM."'

    run_bash_command = BashOperator(
        task_id='run_daily_bash',
        bash_command=bash_command,
    )

    run_bash_command