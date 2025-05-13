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

# Rest of the code remains the same...