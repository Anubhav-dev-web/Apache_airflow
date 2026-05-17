from airflow.sdk import dag, task 
from pendulum import datetime

@dag(
        dag_id="first_schedule_dag",
        start_date= datetime(year=2026, month=5, day=16, tz="Asia/Kolkata"),
        end_date= datetime(year=2026, month=6, day=30, tz="Asia/Kolkata"),
        schedule="@daily",
        is_paused_upon_creation=False,
        catchup=True
)
def first_schedule_dag():

    @task.python
    def first_task():
        print("This is the first task")

    @task.python
    def second_task():
        print("This is the second task")
    
    @task.python
    def third_task():
        print("This is the third task. DAG complete!")
    
    
    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()
    
    first >> second >> third

# Instantiating the DAG
first_schedule_dag()