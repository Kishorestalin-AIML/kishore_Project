def generate_ai_insights(df):
    insights = []

    for col in df.select_dtypes(include="number").columns:
        mean = df[col].mean()
        std = df[col].std()

        if mean > 75:
            level = "strong"
        elif mean > 50:
            level = "average"
        else:
            level = "weak"

        insights.append(
            f"The average value of <b>{col}</b> is {mean:.2f}, indicating <b>{level}</b> performance."
        )

        if std > 15:
            insights.append(
                f"<b>{col}</b> has high variation, showing inconsistent data distribution."
            )

    return insights
