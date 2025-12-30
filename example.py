import pandas as pd

from simple_ds_tools.profiler import profile_dataset
from simple_ds_tools.statistical_analysis import (
    analyze_numeric_columns,
    correlation_analysis
)
from simple_ds_tools.pattern_engine import detect_patterns
from simple_ds_tools.insight_generator import generate_insights


def test_manual_data():
    print("=== TEST: Manual Data ===")

    data = {
        "feature_1": [10, 20, 30, 40, 50],
        "feature_2": [15, 25, 35, 45, 55],
        "category": ["A", "A", "B", "B", "C"]
    }

    df = pd.DataFrame(data)

    profile = profile_dataset(df)
    stats = analyze_numeric_columns(df)
    corr = correlation_analysis(df)
    patterns = detect_patterns(stats, corr)
    insights = generate_insights(profile, patterns)

    for i in insights:
        print("-", i)


if __name__ == "__main__":
    test_manual_data()
