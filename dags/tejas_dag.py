from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag = DAG(
    'simple_bash_dag',
    description='A simple bash command example',
    schedule_interval=None,
    start_date=datetime(2025, 2, 16),
    catchup=False,
)

bash_command = 'echo \"Hello, Airflow!\"'

run_bash_command = BashOperator(
    task_id='run_bash',
    bash_command=bash_command,
    dag=dag,
)

run_bash_command