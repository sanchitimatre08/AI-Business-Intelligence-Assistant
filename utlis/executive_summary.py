from utlis.detector import detect_columns


def generate_executive_summary(df):

    detected = detect_columns(df)

    summary = []

    # Dataset information
    rows, columns = df.shape
    summary.append(
        f"The dataset contains {rows} records and {columns} columns."
    )

    # Top category
    category_col = detected.get("category")
    if category_col:
        top_category = df[category_col].mode()[0]
        summary.append(
            f"The highest-performing category is '{top_category}'."
        )

    # Best-selling product
    product_col = detected.get("product")
    if product_col:
        best_product = df[product_col].mode()[0]
        summary.append(
            f"The best-selling product is '{best_product}'."
        )

    # Preferred payment
    payment_col = detected.get("payment")
    if payment_col:
        payment = df[payment_col].mode()[0]
        summary.append(
            f"Customers mostly prefer '{payment}' for payments."
        )

    # Data quality
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    if missing == 0 and duplicates == 0:
        summary.append(
            "The dataset is clean and ready for analysis."
        )
    else:
        summary.append(
            f"The dataset contains {missing} missing values and {duplicates} duplicate records."
        )

    return " ".join(summary)