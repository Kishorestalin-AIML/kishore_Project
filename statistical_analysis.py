def analyze_numeric_columns(df):
    analysis = {}

    for col in df.select_dtypes(include="number").columns:
        analysis[col] = {
            "mean": df[col].mean(),
            "median": df[col].median(),
            "std": df[col].std(),
            "min": df[col].min(),
            "max": df[col].max()
        }

    return analysis


def correlation_analysis(df):
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return None

    return numeric_df.corr()
