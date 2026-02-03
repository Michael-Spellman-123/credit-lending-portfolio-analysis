import pandas as pd

def create_features(df):
    df = df.copy()

    # Core behavioural ratios
    df["utilisation"] = df["balance"] / df["credit_limit"]
    df["income_to_limit"] = df["annual_income"] / df["credit_limit"]

    # Affordability stress metric
    df["stress_ratio"] = df["balance"] / (df["annual_income"] / 12)

    # Payment behaviour
    df["high_risk_behaviour"] = (
        (df["missed_payments"] > 1).astype(int)
        + (df["utilisation"] > 0.9).astype(int)
    )

    return df
