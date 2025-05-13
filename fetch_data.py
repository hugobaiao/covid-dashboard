# fetch_covid_data.py
import requests
import pandas as pd
from datetime import datetime
from db_connection import get_database_connection
from config import get_config

def fetch_covid_data():
    """Fetch COVID data from disease.sh API"""
    config = get_config()
    
    # Global data
    global_url = config['api']['covid_global_url']
    response = requests.get(global_url)
    global_data = response.json()
    
    # Country data
    countries_url = config['api']['covid_countries_url']
    response = requests.get(countries_url)
    countries_data = response.json()
    
    return global_data, countries_data

def process_global_data(global_data):
    """Process global COVID data"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    global_df = pd.DataFrame([{
        'date': today,
        'total_cases': global_data['cases'],
        'new_cases': global_data['todayCases'],
        'total_deaths': global_data['deaths'],
        'new_deaths': global_data['todayDeaths'],
        'total_recovered': global_data['recovered'],
        'active_cases': global_data['active']
    }])
    
    return global_df

def process_countries_data(countries_data):
    """Process country-specific COVID data"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    countries_list = []
    for country in countries_data:
        countries_list.append({
            'country': country['country'],
            'date': today,
            'total_cases': country['cases'],
            'new_cases': country['todayCases'],
            'total_deaths': country['deaths'],
            'new_deaths': country['todayDeaths'],
            'total_recovered': country['recovered'],
            'active_cases': country['active']
        })
    
    countries_df = pd.DataFrame(countries_list)
    return countries_df

def store_data_in_db(global_df, countries_df, engine):
    """Store processed data in the database"""
    global_df.to_sql('covid_global', engine, if_exists='append', index=False)
    countries_df.to_sql('covid_countries', engine, if_exists='append', index=False)
    print("Data successfully stored in the database")

if __name__ == "__main__":
    # Use the get_database_connection function with config.ini
    engine = get_database_connection()
    
    # Fetch data
    print("Fetching COVID-19 data...")
    global_data, countries_data = fetch_covid_data()
    
    # Process data
    print("Processing global data...")
    global_df = process_global_data(global_data)
    print("Processing country data...")
    countries_df = process_countries_data(countries_data)
    
    # Store data
    print("Storing data in database...")
    store_data_in_db(global_df, countries_df, engine)
    
    print("COVID-19 data update complete!")