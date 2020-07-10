import psycopg2
import sys
import rds_config

def get_connection():
    """
    Create db connection
    """
    db_host = rds_config.db_host
    db_user = rds_config.db_username
    password = rds_config.db_password
    database = rds_config.db_name
    try:
        return psycopg2.connect(
            host = db_host,
            port = 5432,
            user = db_user,
            password = password,
            database = database
        )
    except psycopg2.OperationalError as e:
        print('Unable to make DB connection')
        print(e)
        raise e
    except:
        e = sys.exc_info()[0]
        print("Unexpected error making connection")
        print(e)
        raise e
