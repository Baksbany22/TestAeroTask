from datetime import datetime, timedelta

from airflow.decorators import dag

from tasks import (
     data_recording, insert_in_bd
)


@dag(start_date=datetime(2023, 1, 1),
     schedule_interval=timedelta(hours=12),
     catchup=False,
     render_template_as_native_obj=True,
     orientation='TB',
     default_args={'owner': 'vvasilchikov'},
     tags=[
         "author: vvasilchikov",
         "date_create:17.11.2023"
     ])
def parsing_api_dag():

    data_recording_task = data_recording()

    insert_in_bd_task = insert_in_bd()

    data_recording_task >> insert_in_bd_task


parsing_api_dag = parsing_api_dag()