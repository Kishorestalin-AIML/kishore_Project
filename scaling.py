def min_max_scale(df, column):
    min_val = df[column].min()
    max_val = df[column].max()
    df[column] = (df[column] - min_val) / (max_val - min_val)
    return df

def standard_scale(df, column):
    mean = df[column].mean()
    std = df[column].std()
    df[column] = (df[column] - mean) / std
    return df
