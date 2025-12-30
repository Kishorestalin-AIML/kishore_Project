def label_encode(df, column):
    labels = {val: idx for idx, val in enumerate(df[column].unique())}
    df[column] = df[column].map(labels)
    return df

def one_hot_encode(df, column):
    return df.join(
        __import__("pandas").get_dummies(df[column], prefix=column)
    ).drop(column, axis=1)
