import streamlit as st
import matplotlib.pyplot as plt


# ------------------------------
# Bar Chart
# ------------------------------

def show_bar_chart(df, column):

    data = df[column].value_counts()

    st.bar_chart(data)



# ------------------------------
# Pie Chart
# ------------------------------

def show_pie_chart(df, column):

    data = df[column].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        data,
        labels=data.index,
        autopct="%1.1f%%"
    )

    ax.set_title(column)

    st.pyplot(fig)



# ------------------------------
# Line Chart
# ------------------------------

def show_line_chart(df, column):

    st.line_chart(
        df[column]
    )



# ------------------------------
# Histogram
# ------------------------------

def show_histogram(df, column):

    fig, ax = plt.subplots()

    ax.hist(
        df[column]
    )

    ax.set_title(column)

    st.pyplot(fig)
