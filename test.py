def test_csv_file():
    print("\n=== TEST: CSV File ===")

    df = pd.read_csv("student_data.csv")

    profile = profile_dataset(df)
    stats = analyze_numeric_columns(df)
    corr = correlation_analysis(df)
    patterns = detect_patterns(stats, corr)
    insights = generate_insights(profile, patterns)

    for i in insights:
        print("-", i)
test_csv_file()
