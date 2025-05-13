# analyze_data.py
import pandas as pd
from db_connection import get_database_connection

def run_analytics_queries(engine):
    """Run SQL queries to analyze COVID data"""
    # Query 1: Top 10 countries by total cases
    query1 = """
    SELECT country, MAX(total_cases) as latest_total_cases
    FROM covid_countries
    GROUP BY country
    ORDER BY latest_total_cases DESC
    LIMIT 10
    """
    
    # Query 2: Top 10 countries by mortality rate
    query2 = """
    SELECT country, 
           MAX(total_deaths) as latest_deaths, 
           MAX(total_cases) as latest_cases,
           (MAX(total_deaths) / MAX(total_cases) * 100) as mortality_rate
    FROM covid_countries
    WHERE total_cases > 1000
    GROUP BY country
    ORDER BY mortality_rate DESC
    LIMIT 10
    """
    
    # Query 3: Global trends over time
    query3 = """
    SELECT date, total_cases, total_deaths, total_recovered
    FROM covid_global
    ORDER BY date
    """
    
    # Execute queries
    top_cases = pd.read_sql(query1, engine)
    top_mortality = pd.read_sql(query2, engine)
    global_trends = pd.read_sql(query3, engine)
    
    return top_cases, top_mortality, global_trends

if __name__ == "__main__":
    # Use the get_database_connection function with config.ini
    engine = get_database_connection()
    
    # Run analytics
    top_cases, top_mortality, global_trends = run_analytics_queries(engine)
    
    # Display results
    print("Top 10 Countries by Total Cases:")
    print(top_cases)
    print("\nTop 10 Countries by Mortality Rate:")
    print(top_mortality)
    print("\nGlobal Trends:")
    print(global_trends)