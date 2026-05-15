from airflow.sdk import dag , task

@dag(
    dag_id="versioned_dag",
)
def versioned_dag():
    @task.python  ## Define a Python task
    def first_task():
        print("This is the first task in the DAG!")

    @task.python  ## Define a Python task
    def second_task():
        print("This is the second task in the DAG!")

    @task.python  ## Define a Python task
    def third_task():
        print("This is the third task in the DAG!")

    @task.python  ## Define a Python task
    def versioned_task():
        print("This is the versioned task in the DAG VERSIONED 2.0!")


    first = first_task()  ## Call the first task
    second = second_task()  ## Call the second task
    third = third_task()  ## Call the third task
    version = versioned_task()  ## Call the versioned task

    first >> second >> third >> version  ## Set the task dependencies

versioned_dag()  ## Instantiate the DAG or register it with Airflow 

