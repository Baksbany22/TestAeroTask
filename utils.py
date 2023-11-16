import psycopg2

CON_PARAMS = {'host': 'localhost',
              'user': 'test_user',
              'password': 'test_password',
              'database': 'postgres'}

URL = 'https://random-data-api.com/api/cannabis/random_cannabis?size=10'


class DBHandler:
    """Context manager for psycopg2 connection."""

    def __init__(self, conn_params: dict):
        """Inits object for connect to PostgreSQL database"""

        self._conn_params = conn_params

    def _connect_to_database(self):
        self.connection = psycopg2.connect(**self._conn_params)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __enter__(self):
        return self._connect_to_database()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()


def write_record_into_stg_table(id, uid, strain, cannabinoid_abbreviation, cannabinoid, terpene, medical_use,
                                health_benefit, category, type, buzzword, brand):
    with DBHandler(CON_PARAMS) as cursor:
        cursor.execute(f"""
        INSERT INTO rdv.test_table (
                        id, 
                        uid, 
                        strain, 
                        cannabinoid_abbreviation, 
                        cannabinoid, 
                        terpene, 
                        medical_use,
                        health_benefit, 
                        category, 
                        type, 
                        buzzword, 
                        brand
                    )
                            VALUES (
                        {id}, 
                        {uid}, 
                        {strain}, 
                        {cannabinoid_abbreviation}, 
                        {cannabinoid}, 
                        {terpene}, 
                        {medical_use},
                        {health_benefit}, 
                        {category}, 
                        {type}, 
                        {buzzword}, 
                        {brand}
    );
    """)


