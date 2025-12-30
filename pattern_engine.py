def detect_patterns(stats, corr_matrix):
    patterns = []

    for col, values in stats.items():
        if values["std"] < 0.1:
            patterns.append(f"{col} has very low variance, indicating stable values.")
        elif values["std"] > values["mean"] * 0.5:
            patterns.append(f"{col} shows high variability.")

        if values["mean"] < values["min"] + (values["max"] - values["min"]) * 0.3:
            patterns.append(f"{col} values are skewed towards the lower range.")

    if corr_matrix is not None:
        for i in corr_matrix.columns:
            for j in corr_matrix.columns:
                if i != j:
                    corr = corr_matrix.loc[i, j]
                    if corr > 0.7:
                        patterns.append(
                            f"{i} and {j} have a strong positive relationship."
                        )
                    elif corr < -0.7:
                        patterns.append(
                            f"{i} and {j} have a strong negative relationship."
                        )

    return patterns
