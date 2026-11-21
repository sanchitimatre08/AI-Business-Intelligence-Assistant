def detect_columns(df):
    """
    Automatically detect important business columns.
    """

    columns = {col.lower(): col for col in df.columns}

    keywords = {
        "sales": [
    "total_amount",
    "amount",
    "revenue",
    "sales_amount",
    "total sales",
    "total",
    "price"
    ],

        "quantity": [
            "quantity", "qty", "units"
        ],

        "product": [
            "product", "item", "product_name"
        ],

        "category": [
            "category", "type"
        ],

        "payment": [
            "payment", "payment_mode",
            "payment method"
        ],

        "customer_type": [
            "customer_type", "customer type"
        ],

        "date": [
            "date", "order_date",
            "invoice_date", "datetime"
        ]
    }

    detected = {}

    for field, names in keywords.items():
        detected[field] = None

        for keyword in names:
            for column in columns:
                if column == keyword or column.replace("_", " ") == keyword:
                    detected[field] = columns[column]
                    break

            if detected[field]:
                break

    return detected