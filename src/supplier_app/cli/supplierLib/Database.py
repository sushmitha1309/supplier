import logging
import psycopg2


## Logging Config
LOG = logging.getLogger(__name__)

class Database:

    def connect_database(self, mysql_info):
        """
        Connect database and get local_office table data
        """
        try:
            conn = psycopg2.connect(database="db_name",
                                    host="db_host",
                                    user="db_user",
                                    password="db_pass",
                                    port="db_port")
            cursor = conn.cursor()
            return cursor
        except Exception as e:
            LOG.error(f"An error occurred during connect to DB. {e} ")
            raise SystemExit({"error": e})

    def close_dbconnection(self, db):
        db.cursor().close()
        db.close()


