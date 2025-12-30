def basic_info(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns)
    }

def null_percentage(df):
    return (df.isnull().mean() * 100).to_dict()
