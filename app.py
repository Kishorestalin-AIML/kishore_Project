from flask import Flask, render_template, request
import pandas as pd
import os
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Import the new analysis modules
from simple_ds_tools.profiler import profile_dataset
from simple_ds_tools.statistical_analysis import analyze_numeric_columns, correlation_analysis
from simple_ds_tools.pattern_engine import detect_patterns
from simple_ds_tools.insight_generator import generate_insights

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to generate scatter plot of first two numeric columns
def generate_scatter_plot(df):
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if len(numeric_cols) >= 2:
        x = numeric_cols[0]
        y = numeric_cols[1]

        plt.figure(figsize=(6,4))
        plt.scatter(df[x], df[y], color='blue')
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(f"{y} vs {x}")

        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        plt.close()
        buffer.seek(0)
        image_png = buffer.getvalue()
        encoded = base64.b64encode(image_png).decode("utf-8")
        return encoded
    return None

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]

        if file and file.filename.endswith((".xlsx", ".csv")):
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            # Read CSV or Excel
            if file.filename.endswith(".xlsx"):
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)

            # -----------------------------
            # Analysis Pipeline
            # -----------------------------
            profile = profile_dataset(df)
            stats = analyze_numeric_columns(df)
            corr = correlation_analysis(df)
            patterns = detect_patterns(stats, corr)
            insights = generate_insights(profile, patterns)
            plot = generate_scatter_plot(df)

            # Render report template
            return render_template(
                "report.html",
                tables=df.head().to_html(classes="table", index=False),
                insights=insights,
                plot=plot
            )

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
