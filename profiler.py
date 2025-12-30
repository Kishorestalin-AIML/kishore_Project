def profile_dataset(df):
    profile = {
        "num_rows": df.shape[0],
        "num_cols": df.shape[1],
        "numeric_cols": df.select_dtypes(include="number").columns.tolist(),
        "categorical_cols": df.select_dtypes(exclude="number").columns.tolist(),
        "missing_percent": (df.isnull().mean() * 100).to_dict()
    }
    return profile
