import streamlit as st

# Import Functions
from utlis.loader import load_data
from utlis.cleaning import (
    get_cleaning_report,
    remove_duplicates,
    remove_unnamed_columns,
    handle_missing_values,)
from utlis.metrics import get_dashboard_metrics
from utlis.charts import (
    show_bar_chart,show_pie_chart,
    show_line_chart,show_histogram)
from utlis.dashboard import show_dashboard
from utlis.ai_insights import (generate_ai_insights,generate_ai_recommendations,)
from utlis.filters import apply_filters
from utlis.detector import detect_columns
from utlis.executive_summary import generate_executive_summary
from utlis.business_alerts import generate_business_alerts
from utlis.report_generator import generate_report
from utlis.reports import generate_pdf_report

st.set_page_config(
    page_title="AI Business Intelligence Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Intelligence Assistant")

st.sidebar.title("🧭 Navigation")

st.sidebar.markdown("### 📂 Upload Dataset")

st.sidebar.info(
    "Upload your CSV or Excel dataset to generate business insights."
)

st.sidebar.divider()

st.sidebar.markdown("### 🔍 Dashboard Filters")
# ------------------------------
# Upload Dataset
# ------------------------------

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

# Stop the app until a file is uploaded
if uploaded_file is None:
    st.info("👆 Please upload a dataset to continue.")
    st.stop()
# ------------------------------
# Load Dataset
# ------------------------------

df = load_data(uploaded_file)
# ------------------------------
# Session State
# ------------------------------

# Save the uploaded dataset only if it is a new file
if uploaded_file.name != st.session_state.get("file_name"):

    st.session_state.file_name = uploaded_file.name
    st.session_state.cleaned_df = df.copy()

# Current dataset used everywhere in the app
cleaned_df = st.session_state.cleaned_df
# ------------------------------
# Dataset Preview
# ------------------------------

st.subheader("📄 Dataset Preview")
st.dataframe(cleaned_df.head())
# ------------------------------
# Dataset Size
# ------------------------------

rows, columns = cleaned_df.shape

col1, col2 = st.columns(2)

col1.metric("Rows", rows)
col2.metric("Columns", columns)

# ------------------------------
# Summary Statistics
# ------------------------------

st.subheader("📊 Summary Statistics")

st.dataframe(cleaned_df.describe())
# ------------------------------
# AI Dataset Summary
# ------------------------------

numeric_columns = len(
    cleaned_df.select_dtypes(include="number").columns
)

categorical_columns = len(
    cleaned_df.select_dtypes(exclude="number").columns
)

total_missing = cleaned_df.isnull().sum().sum()

st.subheader("🤖 AI Dataset Summary")

st.info(f"""
📊 Total Rows : **{rows}**

📑 Total Columns : **{columns}**

🔢 Numerical Columns : **{numeric_columns}**

📝 Categorical Columns : **{categorical_columns}**

❗ Total Missing Values : **{total_missing}**
""")
# ------------------------------
# Data Cleaning Report
# ------------------------------

st.subheader("🧹 Data Cleaning Report")

report = get_cleaning_report(cleaned_df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rows", report["Rows"])
col2.metric("Duplicates", report["Duplicate Rows"])
col3.metric("Missing", report["Missing Values"])
col4.metric("Unnamed", report["Unnamed Columns"])
# ------------------------------
# Data Cleaning Options
# ------------------------------

st.subheader("🛠 Data Cleaning")

remove_duplicates_option = st.checkbox("Remove Duplicate Rows")

remove_unnamed_option = st.checkbox("Remove Unnamed Columns")

missing_option = st.selectbox(
    "Handle Missing Values",
    ["None", "Mean", "Median", "Mode", "Drop"]
)
# ------------------------------
# Apply Cleaning
# ------------------------------

if st.button("🧹 Apply Cleaning"):

    # Start with the current dataset
    cleaned_df = st.session_state.cleaned_df.copy()

    # Remove duplicate rows
    if remove_duplicates_option:
        cleaned_df = remove_duplicates(cleaned_df)

    # Remove unnamed columns
    if remove_unnamed_option:
        cleaned_df = remove_unnamed_columns(cleaned_df)

    # Handle missing values
    if missing_option != "None":
        cleaned_df = handle_missing_values(
            cleaned_df,
            missing_option
        )

    # Save cleaned dataset
    st.session_state.cleaned_df = cleaned_df

    st.success("✅ Data cleaned successfully!")

# ------------------------------
# Cleaned Dataset Preview
# ------------------------------

st.subheader("📄 Cleaned Dataset")

st.dataframe(st.session_state.cleaned_df.head())
# ------------------------------
# Download Cleaned Dataset
# ------------------------------

st.download_button(
    "📥 Download Cleaned Dataset",
    st.session_state.cleaned_df.to_csv(index=False),
    "cleaned_dataset.csv",
    "text/csv"
)
detected = detect_columns(
    st.session_state.cleaned_df
)

filtered_df = apply_filters(
    st.session_state.cleaned_df,
    detected
)
if filtered_df.empty:
    st.warning("⚠ No data available for the selected filters.")
    st.stop()
report = generate_report(filtered_df)
# ------------------------------
# Executive Summary
# ------------------------------

with st.container():

    st.header("📋 Executive Summary")

    summary = generate_executive_summary(filtered_df)

    st.info(summary)

st.divider()
# ------------------------------
# Business Alerts
# ------------------------------

with st.container():

    st.header("🚨 Business Alerts")

    alerts = generate_business_alerts(filtered_df)

    for alert in alerts:
        st.warning(alert)

st.divider()
# ------------------------------
# Dashboard
# ------------------------------
with st.container():

    show_dashboard(filtered_df)

st.divider()
# ------------------------------
# AI Business Insights
# ------------------------------

with st.container():

    st.header("🤖 AI Business Insights")

    insights = generate_ai_insights(filtered_df)

    for insight in insights[:5]:
        st.info(insight)

st.divider()

# ------------------------------
# AI Business Recommendations
# ------------------------------

with st.container():

    st.header("💡 AI Business Recommendations")

    recommendations = generate_ai_recommendations(filtered_df)

    for recommendation in recommendations[:5]:
        st.info(recommendation)

st.divider()
# ------------------------------
# Download AI Business Report
# ------------------------------

with st.container():

    st.header("📥 Download AI Report")

    executive_summary = [
        f"Dataset contains {len(filtered_df)} records.",
        f"Dataset has {filtered_df.shape[1]} columns.",
        "Business insights generated successfully."
    ]

    business_alerts = []

    missing = filtered_df.isnull().sum().sum()

    if missing > 0:
        business_alerts.append(f"Missing Values: {missing}")
    else:
        business_alerts.append("No missing values detected.")

    duplicates = filtered_df.duplicated().sum()

    if duplicates > 0:
        business_alerts.append(f"Duplicate Records: {duplicates}")
    else:
        business_alerts.append("No duplicate records detected.")
    kpi_data = {
    "Total Records": f"{len(filtered_df):,}",
    "Total Columns": filtered_df.shape[1],
    "Missing Values": filtered_df.isnull().sum().sum(),
    "Duplicate Records": filtered_df.duplicated().sum()
}

    pdf = generate_pdf_report(
        executive_summary,
        business_alerts,
        insights,
        recommendations,
        kpi_data
)
    st.download_button(
        label="📄 Download AI Report (PDF)",
        data=pdf,
        file_name="AI_Business_Report.pdf",
        mime="application/pdf"
    )