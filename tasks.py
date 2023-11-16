from airflow.decorators import task

from utils import write_record_into_stg_table, URL

import requests
import json


@task
def data_recording():
    response = requests.get(URL).content.decode('utf-8')
    try:
        data = json.loads(response)
    except:
        raise Exception('This object is not JSON')
    return data


@task
def insert_in_bd():
    data = {'data':'task_instance.xcom_pull(task_ids="data_recording"}}'}
    for row in data[data]:
        write_record_into_stg_table(
            id=row['id'],
            uid=row['uid'],
            strain=row['strain'],
            cannabinoid_abbreviation=row['cannabinoid_abbreviation'],
            cannabinoid=row['cannabinoid'],
            terpene=row['terpene'],
            medical_use=['medical_use'],
            health_benefit=['health_benefit'],
            category=['category'],
            type=['type'],
            buzzword=['buzzword'],
            brand=['brand']
        )
