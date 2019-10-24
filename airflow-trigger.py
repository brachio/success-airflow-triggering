from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from datetime import datetime


def my_python_callable(**context):
    print(context['ts'])


args = {
    'owner': 'airflow',
    'start_date': datetime(2019, 6, 20),
}

dag = DAG(
    dag_id="control_dag",
    # DAG의 동시 실행을 방지한다.
    max_active_runs=1,
    default_args=args,
    # 분 시 일 월 요일
    # 매월 15일 오전 10시 정각에 구동
    schedule_interval=None,
)

TriggerDagRunOperator(
    task_id='trigger',
    trigger_dag_id='target_dag',
    start_date=datetime(1992,11,2,10,0),
    execution_date=datetime(1992,11,3,10,0),
    dag=dag,
)
