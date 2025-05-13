# COVID-19 Data Dashboard

A data analytics project that fetches COVID-19 data, stores it in a MariaDB database, and visualizes key metrics using Python and Streamlit.

## My Insights

Based on data collected on May 14, 2025, our analysis reveals several key patterns in the global COVID-19 landscape:

### Case Distribution Analysis

**Highest Case Concentrations:**
The United States continues to lead with over 111.8 million total cases, followed by India (45 million), France (40.1 million), Germany (38.8 million), and Brazil (38.7 million). This concentration in high-population, highly-connected countries follows established epidemiological patterns for respiratory diseases.

**Lowest Case Regions:**
Regions with minimal reported cases include MS Zaandam (9), Western Sahara (10), Vatican City (29), and Tokelau (80). These figures likely reflect a combination of geographic isolation, low population density, and potentially limited testing infrastructure rather than actual infection rates.

### Mortality Analysis

**Highest Mortality Burden:**
The countries experiencing the greatest absolute mortality impact are the United States (1.2 million deaths), Brazil (711,380 deaths), India (533,570 deaths), Russia (402,756 deaths), and Mexico. This demonstrates the pandemic's profound impact on both developed and developing healthcare systems.

### Recovery Patterns

**Most Documented Recoveries:**
Recovery tracking shows the United States leading with 109.8 million recoveries, followed by France (40 million), Germany (38.2 million), Brazil (36.2 million), and South Korea. These figures highlight different approaches to recovery documentation and healthcare follow-up practices among countries.

*Note: Data quality varies significantly between countries due to differences in testing protocols, reporting methodologies, and healthcare infrastructure.*

## Setup

1. Clone the repository: git clone https://github.com/your-username/covid-dashboard.git
cd covid-dashboard

2. Install the required packages: pip install -r requirements.txt

3. Create a configuration file: cp config.sample.ini config.ini

4. Edit `config.ini` with your database credentials.

5. Set up the database schema: python create_schema.py

6. Fetch covid data: python fetch_covid_data.py

7. Run the dashboard: streamlit run dashboard.py

## Features

- Fetches real-time COVID-19 data from disease.sh API
- Stores data in a MariaDB database
- Analyzes data using SQL queries
- Visualizes key metrics with Matplotlib and Seaborn
- Provides an interactive dashboard with Streamlit

## Tools Used

- Python
- Pandas
- SQLAlchemy
- MariaDB
- Matplotlib/Seaborn
- Streamlit
