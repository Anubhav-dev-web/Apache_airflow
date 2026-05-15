from airflow.sdk import dag , task

@dag(
    dag_id="first_dag",
)
def first_dag():
    @task.python  ## Define a Python task
    def first_task():
        print("This is the first task in the DAG!")

    @task.python  ## Define a Python task
    def second_task():
        print("This is the second task in the DAG!")

    @task.python  ## Define a Python task
    def third_task():
        print("This is the third task in the DAG!")


    first = first_task()  ## Call the first task
    second = second_task()  ## Call the second task
    third = third_task()  ## Call the third task

    first >> second >> third  ## Set the task dependencies

first_dag()  ## Instantiate the DAG or register it with Airflow 

