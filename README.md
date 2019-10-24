# success-airflow-triggering
airflow triggering success.
airflow에서 DAG A에서 DAG B를 specific date로 구동시키는 것을 성공했다.
이를 기록한다. 

> 이것을 테스트하면서 얻은 교훈이 있다.
> Trigger되는 DAG의 schedule_interval이 None(즉, externally trigger될 DAG)이라도, start_date 날짜보다 하루 뒤 날짜에 시작된다.
> execution_date와 start_date의 날짜가 모두 동일하다면 Trigger된 DAG은 operator들을 수행하지 않고, 그냥 종료된다.
> 즉 execution_date는 start_date보다 항상 하루(24시간)이상의 값이 커야한다.
> 이를 위해 externally triggered 될 DAG은, 애초에 start_date 값을 작게 잡아 놓는게, trigger 하는 입장에서 원하는 날짜에 구동되도록 할 수 있다.
