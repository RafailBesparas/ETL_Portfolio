from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define DAG arguments
default_args = {
    'owner': 'RafaelBesparas',  # Replace with your name
    'start_date': datetime.today(),
    'email': 'your.email@example.com',  # Replace with your email
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5), # Import timedelta
}

# Define the DAG ID and the Description
dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval='@daily',  # Corrected schedule interval
    default_args=default_args,
    description='Apache Project on Using Airflow for Automating ETL',
)

# Log the project path for where the etl will work on the directory and folders
project_path = "C:\Users\user\Desktop\Showcase\ETLKafkaAndApacheSpark"  


# Define the tasks of unziping the data 
unzip_data = BashOperator(
    task_id='unzip_data',
        bash_command=f"tar -xzf {project_path}\\tolldata.tgz -C {project_path}",  # Use f-string and \\ for Windows paths, 
    dag=dag,
)


# Extract the data from the vehicle.csv
extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command=f"cut -d',' -f1,2,3,4 {project_path}\\vehicle-data.csv > {project_path}\\csv_data.csv",
    dag=dag,
)

# Extract the data from a tsv file 
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command=f"cut -f1,2,3 {project_path}\\tollplaza-data.tsv > {project_path}\\tsv_data.csv",
    dag=dag,
)

# Extract the data from the payment data
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command=f"cut -c 1-2, 9-10 {project_path}\\payment-data.txt > {project_path}\\fixed_width_data.csv",
    dag=dag,
)

# Put the data into one destination 
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command=f"paste {project_path}\\csv_data.csv {project_path}\\tsv_data.csv {project_path}\\fixed_width_data.csv > {project_path}\\extracted_data.csv",
    dag=dag,
)

# Transform the data according to the exercise
transform_data = BashOperator(
    task_id='transform_data',
    bash_command=f"tr '[:lower:]' '[:upper:]' < {project_path}\\extracted_data.csv > {project_path}\\transformed_data.csv",
    dag=dag,
)

# Task Pipelines
# Define the task pipeline
unzip_data >> extract_data_from_csv
unzip_data >> extract_data_from_tsv
unzip_data >> extract_data_from_fixed_width
extract_data_from_csv >> consolidate_data
extract_data_from_tsv >> consolidate_data
extract_data_from_fixed_width >> consolidate_data
consolidate_data >> transform_data
