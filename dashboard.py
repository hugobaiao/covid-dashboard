# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analyze_data import run_analytics_queries
from db_connection import get_database_connection

def main():
    st.title("COVID-19 Data Dashboard")
    
    # Connect to database using config.ini
    engine = get_database_connection()
    
    # Run analytics
    top_cases, top_mortality, global_trends = run_analytics_queries(engine)
    
    # Display global statistics
    st.header("Global COVID-19 Statistics")
    if not global_trends.empty:
        latest_global = global_trends.iloc[-1]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Cases", f"{latest_global['total_cases']:,}")
        with col2:
            st.metric("Total Deaths", f"{latest_global['total_deaths']:,}")
        with col3:
            st.metric("Total Recovered", f"{latest_global['total_recovered']:,}")
    else:
        st.warning("No global data available yet. Please run fetch_covid_data.py first.")
    
    # Top countries by cases
    st.header("Top 10 Countries by Total Cases")
    if not top_cases.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="latest_total_cases", y="country", data=top_cases, ax=ax)
        plt.title("Top 10 Countries by Total COVID-19 Cases")
        plt.xlabel("Total Cases")
        plt.ylabel("Country")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("No country case data available yet.")
    
    # Top countries by mortality
    st.header("Top 10 Countries by Mortality Rate")
    if not top_mortality.empty:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x="mortality_rate", y="country", data=top_mortality, ax=ax)
        plt.title("Top 10 Countries by COVID-19 Mortality Rate")
        plt.xlabel("Mortality Rate (%)")
        plt.ylabel("Country")
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("No mortality rate data available yet.")
    
    # Global trends
    st.header("Global COVID-19 Trends")
    if not global_trends.empty and len(global_trends) > 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.plot(global_trends['date'], global_trends['total_cases'], label='Total Cases')
        plt.plot(global_trends['date'], global_trends['total_deaths'], label='Total Deaths')
        plt.plot(global_trends['date'], global_trends['total_recovered'], label='Total Recovered')
        plt.title("Global COVID-19 Trends")
        plt.xlabel("Date")
        plt.ylabel("Count")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)
    else:
        st.warning("Not enough time-series data available yet for trend visualization.")
    
    # Raw data
    st.header("Raw Data")
    if st.checkbox("Show country data"):
        st.subheader("Country Data")
        query = """
        SELECT country, date, total_cases, new_cases, total_deaths, new_deaths
        FROM covid_countries
        ORDER BY total_cases DESC
        LIMIT 100
        """
        country_data = pd.read_sql(query, engine)
        st.dataframe(country_data)

if __name__ == "__main__":
    main()