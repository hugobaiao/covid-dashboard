# create_schema.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date
from db_connection import get_database_connection

def create_covid_tables(engine):
    """Create tables for COVID data if they don't exist"""
    metadata = MetaData()
    
    # Table for global COVID data
    covid_global = Table(
        'covid_global', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('date', Date, nullable=False),
        Column('total_cases', Integer),
        Column('new_cases', Integer),
        Column('total_deaths', Integer),
        Column('new_deaths', Integer),
        Column('total_recovered', Integer),
        Column('active_cases', Integer)
    )
    
    # Table for country-specific COVID data
    covid_countries = Table(
        'covid_countries', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('country', String(100), nullable=False),
        Column('date', Date, nullable=False),
        Column('total_cases', Integer),
        Column('new_cases', Integer),
        Column('total_deaths', Integer),
        Column('new_deaths', Integer),
        Column('total_recovered', Integer),
        Column('active_cases', Integer)
    )
    
    # Create tables in the database
    metadata.create_all(engine)
    print("Database tables created successfully")

if __name__ == "__main__":
    # Use the get_database_connection function with config.ini
    engine = get_database_connection()
    create_covid_tables(engine)