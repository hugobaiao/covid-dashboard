# config.py
import configparser
import os

def get_config():
    """Read configuration from config.ini file"""
    config = configparser.ConfigParser()
    
    # Determine the directory this script is in
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.ini')
    
    # Check if config file exists
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at {config_path}")
    
    config.read(config_path)
    return config