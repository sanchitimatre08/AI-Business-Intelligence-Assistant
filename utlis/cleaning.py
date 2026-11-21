import pandas as pd
def get_cleaning_report(df):
    """
    Generate a report about the dataset before cleaning.
    """

    report = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Duplicate Rows": df.duplicated().sum(),
        "Unnamed Columns": len(
            [col for col in df.columns if "Unnamed" in str(col)]
        ),
        "Missing Values": df.isnull().sum().sum(),
    }
    return report

def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates()

def remove_unnamed_columns(df):
    """
    Remove columns like 'Unnamed: 0'.
    """
    return df.loc[:, ~df.columns.str.contains("^Unnamed")]

def handle_missing_values(df, method):
    """
    Handle missing values based on the user's selected method.
    """
    # Create a copy to avoid modifying the original dataframe
    df = df.copy()
    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include="number").columns
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns
    # Mean
    if method == "Mean":
        df[numeric_cols] = df[numeric_cols].fillna(
            df[numeric_cols].mean()
        )
        df[categorical_cols] = df[categorical_cols].fillna("Unknown")
    # Median
    elif method == "Median":
        df[numeric_cols] = df[numeric_cols].fillna(
            df[numeric_cols].median()
        )
        df[categorical_cols] = df[categorical_cols].fillna("Unknown")
    # Mode
    elif method == "Mode":
        for col in df.columns:
            mode = df[col].mode()

            if not mode.empty:
                df[col] = df[col].fillna(mode.iloc[0])
    # Drop rows containing missing values
    elif method == "Drop":
        df = df.dropna()

    return df