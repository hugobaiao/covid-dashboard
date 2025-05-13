# visualize_data.py
import matplotlib.pyplot as plt
import seaborn as sns
from analyze_data import run_analytics_queries
from db_connection import get_database_connection

def create_visualizations(top_cases, top_mortality, global_trends):
    """Create visualizations for COVID data analysis"""
    # Set style
    sns.set(style="whitegrid")
    
    # Figure 1: Top countries by cases
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x="latest_total_cases", y="country", data=top_cases)
    plt.title("Top 10 Countries by Total COVID-19 Cases")
    plt.xlabel("Total Cases")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig("top_cases.png")
    
    # Figure 2: Top countries by mortality rate
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x="mortality_rate", y="country", data=top_mortality)
    plt.title("Top 10 Countries by COVID-19 Mortality Rate")
    plt.xlabel("Mortality Rate (%)")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig("mortality_rate.png")
    
    # Figure 3: Global trends
    plt.figure(figsize=(12, 6))
    plt.plot(global_trends['date'], global_trends['total_cases'], label='Total Cases')
    plt.plot(global_trends['date'], global_trends['total_deaths'], label='Total Deaths')
    plt.plot(global_trends['date'], global_trends['total_recovered'], label='Total Recovered')
    plt.title("Global COVID-19 Trends")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("global_trends.png")
    
    print("Visualizations created and saved")

if __name__ == "__main__":
    # Use the get_database_connection function with config.ini
    engine = get_database_connection()
    
    # Run analytics
    top_cases, top_mortality, global_trends = run_analytics_queries(engine)
    
    # Create visualizations
    create_visualizations(top_cases, top_mortality, global_trends)