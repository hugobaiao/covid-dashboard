# COVID-19 Data Dashboard

A data analytics project that fetches COVID-19 data, stores it in a MariaDB database, and visualizes key metrics using Python and Streamlit.

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
