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

def clean_data(df):
    """Clean the merged dataframe to make it ready to analyze"""
    
    # Create column based on values in categories column
    categories = df['categories'].str.split(';', expand=True)

    # Rename the columns with the proper name
    row = categories.loc[0,:]
    category_colnames = row.apply(lambda x: x.split('-')[0]).tolist()
    categories.columns = category_colnames

    # Clean the value in categories
    for column in categories:

        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x.split('-')[1])
        
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    categories['related'] = categories['related'].replace(2, 1)

    # Replace the original categories column with the new one and drop duplicates
    df.drop(columns=['categories'], inplace=True)
    df = pd.concat([df, categories], axis=1)
    df.drop_duplicates(inplace=True)

    return df