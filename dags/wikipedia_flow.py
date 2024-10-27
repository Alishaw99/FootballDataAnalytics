import os
import sys
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.wikipedia_pipeline import get_wikipedia_page

dag = DAG(
    dag_id = 'wikipedia_flow',

    default_args={

        "owner": "Tariq Ali"
        "start_date": datetime(year:2024, month:10, day:1),
    },

    "schedule_interview"=None,
    catchup=False

)


extract_data_from_wikipedia = PythonOperator (
    task_id = "extract_data_from_wikipedia",
    python_callable=get_wikipedia_page,
    provide_context=True
    op_kwargs={"url": "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"},
    dag=dag

)
# Preprocessing
# write