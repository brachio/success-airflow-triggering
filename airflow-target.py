from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime


def my_python_callable(**context):
    print("check111")
    print(context['ts'])
    print("check222")

args = {
    'owner': 'airflow',
    'start_date': datetime(999,11,8,10,0),
}

dag = DAG(
    dag_id="target_dag",
    # DAG의 동시 실행을 방지한다.
    max_active_runs=1,
    default_args=args,
    # 분 시 일 월 요일
    # 매월 15일 오전 10시 정각에 구동
    schedule_interval=None,
)

start = DummyOperator(
    task_id='start',
    default_args=args,
    dag=dag,
)

second = PythonOperator(
    task_id='called',
    python_callable=my_python_callable,
    provide_context=True,
    dag=dag,
)

start >> second
