from utlis.detector import detect_columns


def generate_business_alerts(df):

    alerts = []

    detected = detect_columns(df)

    sales_col = detected.get("sales")
    category_col = detected.get("category")
    payment_col = detected.get("payment")

    # --------------------------
    # Revenue Alert
    # --------------------------

    if sales_col:

        total_sales = df[sales_col].sum()

        if total_sales > 100000:
            alerts.append(
                "📈 High revenue detected. Business performance is strong."
            )
        else:
            alerts.append(
                "📉 Revenue is relatively low. Consider improving sales strategies."
            )

    # --------------------------
    # Category Alert
    # --------------------------

    if category_col:

        top_category = df[category_col].mode()[0]

        alerts.append(
            f"🏆 '{top_category}' is currently the highest-performing category."
        )

    # --------------------------
    # Payment Alert
    # --------------------------

    if payment_col:

        payment = df[payment_col].mode()[0]

        alerts.append(
            f"💳 Most customers prefer '{payment}' as their payment method."
        )

    # --------------------------
    # Missing Values Alert
    # --------------------------

    missing = df.isnull().sum().sum()

    if missing > 0:
        alerts.append(
            f"⚠ Dataset contains {missing} missing values."
        )
    else:
        alerts.append(
            "✅ No missing values detected."
        )

    # --------------------------
    # Duplicate Records Alert
    # --------------------------

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        alerts.append(
            f"🧹 Dataset contains {duplicates} duplicate records."
        )
    else:
        alerts.append(
            "✅ No duplicate records found."
        )

    return alerts