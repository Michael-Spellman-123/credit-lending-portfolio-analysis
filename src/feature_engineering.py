import pandas as pd

def create_features(df):
    df = df.copy()
    df["utilisation"] = df["balance"] / df["credit_limit"]
    df["income_to_loan"] = df["annual_income"] / df["loan_amount"]
    return df