def generate_insights(profile, patterns):
    insights = []

    insights.append(
        f"The dataset contains {profile['num_rows']} rows and {profile['num_cols']} columns."
    )

    if profile["numeric_cols"]:
        insights.append(
            f"Numeric features detected: {', '.join(profile['numeric_cols'])}."
        )

    if profile["categorical_cols"]:
        insights.append(
            f"Categorical features detected: {', '.join(profile['categorical_cols'])}."
        )

    insights.extend(patterns)

    return insights
