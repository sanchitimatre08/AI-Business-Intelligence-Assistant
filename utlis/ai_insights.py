import pandas as pd
from utlis.detector import detect_columns


def generate_ai_insights(df):

    insights = []

    detected = detect_columns(df)

    sales_col = detected.get("sales")
    product_col = detected.get("product")
    category_col = detected.get("category")
    payment_col = detected.get("payment")
    quantity_col = detected.get("quantity")

    # ==========================
    # Revenue Insight
    # ==========================
    if sales_col:
        total_revenue = df[sales_col].sum()
        insights.append(
            f"📈 Total revenue generated is ₹{total_revenue:,.2f}."
        )

    # ==========================
    # Best Selling Product
    # ==========================
    if product_col:
        best_product = df[product_col].mode()[0]
        insights.append(
            f"🏆 '{best_product}' is the best-selling product."
        )

    # ==========================
    # Top Category
    # ==========================
    if category_col:
        top_category = df[category_col].mode()[0]
        insights.append(
            f"📊 '{top_category}' is the highest-performing category."
        )

    # ==========================
    # Customer Preference
    # ==========================
    if payment_col:
        payment = df[payment_col].mode()[0]
        insights.append(
            f"💳 Customers mostly prefer '{payment}' as the payment method."
        )

    # ==========================
    # Purchase Behaviour
    # ==========================
    if quantity_col:
        avg_qty = df[quantity_col].mean()
        insights.append(
            f"📦 Customers purchase an average of {avg_qty:.1f} items per order."
        )

    # ==========================
    # Data Quality Alert
    # ==========================
    missing = df.isnull().sum().sum()

    if missing > 0:
        insights.append(
            f"⚠ Dataset contains {missing} missing values that may affect analysis."
        )

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        insights.append(
            f"🧹 Dataset contains {duplicates} duplicate records."
        )

    return insights

def generate_ai_recommendations(df):

    recommendations = []

    detected = detect_columns(df)

    sales_col = detected.get("sales")
    product_col = detected.get("product")
    category_col = detected.get("category")
    payment_col = detected.get("payment")

    # ==========================
    # Revenue Recommendation
    # ==========================
    if sales_col:
        recommendations.append(
            "📈 Monitor revenue trends regularly to identify growth opportunities."
        )

    # ==========================
    # Product Recommendation
    # ==========================
    if product_col:
        top_product = df[product_col].mode()[0]

        recommendations.append(
            f"🛒 Maintain sufficient inventory for '{top_product}' to avoid stock shortages."
        )

    # ==========================
    # Category Recommendation
    # ==========================
    if category_col:
        top_category = df[category_col].mode()[0]

        recommendations.append(
            f"📂 Focus marketing efforts on the '{top_category}' category to maximize revenue."
        )

    # ==========================
    # Payment Recommendation
    # ==========================
    if payment_col:
        payment = df[payment_col].mode()[0]

        recommendations.append(
            f"💳 Continue supporting '{payment}' as it is the preferred payment method."
        )

    # ==========================
    # Data Quality Recommendation
    # ==========================
    missing = df.isnull().sum().sum()

    if missing > 0:
        recommendations.append(
            "⚠ Resolve missing values before making business decisions."
        )

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        recommendations.append(
            "🧹 Remove duplicate records to improve analysis accuracy."
        )

    return recommendations