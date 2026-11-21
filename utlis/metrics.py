def get_dashboard_metrics(df):

    return {
        "Total Rows": df.shape[0],
        "Total Columns": df.shape[1],
        "Numerical Columns": len(df.select_dtypes(include="number").columns),
        "Categorical Columns": len(df.select_dtypes(exclude="number").columns),
        "Missing Values": df.isnull().sum().sum()
    }