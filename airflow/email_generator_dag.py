# import faker
# import random
import datetime
from airflow import DAG
from ..subsription_event import generate_emails
from airflow.operators.python import PythonOperator


# fake = faker.Faker()

# def generate_emails():

#     first_name = fake.first_name()
#     last_name = fake.last_name()
#     dm_weights = [0.5, 0.2, 0.05, 0.05, 0.2]
#     domain = random.choices(["gmail", "outlook", "hotmail", "yahoo", "icloud"], dm_weights, k = 1)
#     extension = random.choice(["com", "co.uk", "org"])
#     email = f"{first_name}{last_name}@{domain[0]}.{extension}"

#     return [first_name, last_name, email]

args = {
    'owner': 'Victor',
    'start_date': datetime.datetime(2025, 2, 19),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes = 5)
}

dag = DAG(
    'email_generator_dag',
    default_args = args,
    description = 'Generates a random email address every hour.',
    schedule_interval = '0 * * * *',
    catchup = False 
)

generate_emails_task = PythonOperator(
    task_id = 'generate_emails_task',
    python_callable = generate_emails,
    dag = dag
)

# airflow users create \
#     --username admin \
#     --firstname Victor \
#     --lastname Agbeleye \
#     --role Admin \
#     --email victoragbeleye2@gmail.com \
#     --password abo200313