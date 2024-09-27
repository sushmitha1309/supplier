import logging
import psycopg2
import pyodbc


## Logging Config
LOG = logging.getLogger(__name__)

class Database:

    def connect_database(self, mysql_info):
        """
        Connect database and get local_office table data
        """
        try:
            # conn = psycopg2.connect(database="supplier_database",
            #                         host="localhost",
            #                         user="postgres",
            #                         password="admin",
            #                         port="5432")
            conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=VPA10L-0481W9P\SQLEXPRESS;"
                      "Database=supplier;"
                      "Trusted_Connection=yes;")
            cursor = conn.cursor()
            return cursor, conn
        except Exception as e:
            LOG.error(f"An error occurred during connect to DB. {e} ")
            raise SystemExit({"error": e})


    def close_dbconnection(self, db):
        db.cursor().close()
        db.close()


