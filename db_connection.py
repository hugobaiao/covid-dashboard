# db_connection.py
from sqlalchemy import create_engine
import pandas as pd
from config import get_config

def get_database_connection():
    """Create a connection to the MariaDB database using config.ini"""
    config = get_config()
    
    user = config['database']['user']
    password = config['database']['password']
    host = config['database']['host']
    port = config['database']['port']
    db_name = config['database']['db_name']
    
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}"
    engine = create_engine(connection_string)
    return engine

# Test connection
if __name__ == "__main__":
    engine = get_database_connection()
    try:
        with engine.connect() as conn:
            print("Successfully connected to MariaDB!")
    except Exception as e:
        print(f"Error connecting to database: {e}")