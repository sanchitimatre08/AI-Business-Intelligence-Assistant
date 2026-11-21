import streamlit as st

from utlis.metrics import get_dashboard_metrics
from utlis.charts import (
    show_bar_chart,
    show_pie_chart,
    show_line_chart,
    show_histogram,
)


def show_dashboard(df):

    # ---------------- Dashboard ---------------- #
    st.header("📊 Dashboard")

    metrics = get_dashboard_metrics(df)

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("📄 Total Records", f"{metrics['Total Rows']:,}")
    c2.metric("📋 Total Columns", metrics["Total Columns"])
    c3.metric("🔢 Numeric Fields", metrics["Numerical Columns"])
    c4.metric("📝 Categorical Fields", metrics["Categorical Columns"])
    c5.metric("⚠ Missing Values", metrics["Missing Values"])
    st.divider()

    # ---------------- Interactive Charts ---------------- #

    st.header("📈 Business Visualizations")


    text_columns = df.select_dtypes(include="object").columns.tolist()
    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:

        st.subheader("📊 Category Distribution")

        if text_columns:

            bar_col = st.selectbox(
                "Category",
                text_columns,
                key="bar_chart"
            )

            show_bar_chart(df, bar_col)

    with row1_col2:

        st.subheader("🥧 Payment / Category Share")

        if text_columns:

            pie_col = st.selectbox(
                "Category ",
                text_columns,
                key="pie_chart"
            )

            show_pie_chart(df, pie_col)

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:

        st.subheader("📈 Revenue Trend")

        if numeric_columns:

            line_col = st.selectbox(
                "Numeric Column",
                numeric_columns,
                key="line_chart"
            )

            show_line_chart(df, line_col)

    with row2_col2:

        st.subheader("📉 Numeric Distribution")

        if numeric_columns:

            hist_col = st.selectbox(
                "Numeric Column ",
                numeric_columns,
                key="hist_chart"
            )

            show_histogram(df, hist_col)