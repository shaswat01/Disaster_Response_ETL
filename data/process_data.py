from sqlalchemy import create_engine
import pandas as pd
import sys

def load_data(messages_filepath, categories_filepath):
    """Read messages and categories data and merge it into one dataframe"""

    # Read messages and categories data
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # Merge the two dataframes
    df = messages.merge(categories, on='id')
    
    return df

