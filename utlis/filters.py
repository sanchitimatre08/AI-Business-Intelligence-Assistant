import streamlit as st


def apply_filters(df, detected):

    filtered_df = df.copy()

    # --------------------------
    # Category Filter
    # --------------------------
    category_col = detected.get("category")
    

    if category_col:

        categories = ["All"] + sorted(
            filtered_df[category_col].dropna().unique().tolist()
        )

        selected_category = st.sidebar.selectbox(
            "Category",
            categories
        )

        if selected_category != "All":
            filtered_df = filtered_df[
                filtered_df[category_col] == selected_category
            ]

    # --------------------------
    # Payment Filter
    # --------------------------

    payment_col = detected.get("payment")

    if payment_col:

        payments = ["All"] + sorted(
            filtered_df[payment_col].dropna().unique().tolist()
        )

        selected_payment = st.sidebar.selectbox(
            "Payment Method",
            payments
        )

        if selected_payment != "All":
            filtered_df = filtered_df[
                filtered_df[payment_col] == selected_payment
            ]

    return filtered_df