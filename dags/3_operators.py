from airflow.sdk import dag , task
from airflow.operators.bash import BashOperator


@dag(
    dag_id="operators_dag",
)
def operators_dag():
    @task.python  ## Define a Python task
    def first_task():
        print("This is the first task in the DAG!")

    @task.python  ## Define a Python task
    def second_task():
        print("This is the second task in the DAG!")

    @task.bash
    def bash_task_modern():
        return "echo https://airflow.apache.org/" ## Return a bash command as a string
    
    bash_task_oldschool = BashOperator(
    task_id="bash_task_oldschool",
    bash_command="echo https://airflow.apache.org/",
    )


    first = first_task()  ## Call the first task
    second = second_task()  ## Call the second task
    third = bash_task_modern()  ## Call the third bash task
    fourth = bash_task_oldschool  ## Reference the old school bash task

    first >> second >> third  ## Set the task dependencies

operators_dag()  ## Instantiate the DAG or register it with Airflow 

