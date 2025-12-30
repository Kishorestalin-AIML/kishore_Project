import pandas as pd

def remove_nulls(df):
    return df.dropna()

def fill_missing_mean(df, column):
    df[column] = df[column].fillna(df[column].mean())
    return df

def fill_missing_median(df, column):
    df[column] = df[column].fillna(df[column].median())
    return df

def fill_missing_mode(df, column):
    df[column] = df[column].fillna(df[column].mode()[0])
    return df
