"""
data_cleaning.py
----------------
Purpose:
    This script loads a messy sales dataset, applies a structured sequence
    of data cleaning steps, and exports a cleaned version of the CSV.
    It demonstrates beginner-friendly data cleaning techniques in Python
    and prepares the dataset for analysis or visualization.
"""

import pandas as pd




# 1. Load the raw dataset
# What: Load the CSV file from the data/raw folder.
# Why: We need the raw data in memory before cleaning it.
# ---------------------------------------------------
# Function: load_data 
# This function should load a CSV file from disk and return a DataFrame.
def load_data(file_path):
    """Load a CSV file and return a pandas DataFrame."""
    return pd.read_csv(file_path)



# 2. Standardize column names
# What: Convert names to lowercase and replace spaces with underscores.
# Why: Consistent column names prevent bugs and make the dataset easier to use.

def clean_column_names(df):
    """Standardize column names: lowercase + underscores + strip spaces."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


# 3. Strip whitespace from string columns
# What: Remove leading/trailing spaces from product names & categories.
# Why: Prevents duplicate categories like "Fruits" vs "Fruits ".

def strip_whitespace(df):
    """Strip whitespace from all string (object) columns."""
    df = df.copy()
    string_cols = df.select_dtypes(include="object").columns
    df[string_cols] = df[string_cols].apply(lambda col: col.str.strip())
    return df



# 4. Handle missing prices and quantities
# What: Fill missing values with 0 (or change to drop if you prefer).
# Why: Missing numeric values cause errors in analysis and calculations.

def handle_missing_values(df):
    """Fill missing price/quantity values with 0."""
    df = df.copy()

    # Convert to numeric to fix issues like '$4.99' or invalid characters
    for col in ["price", "quantity"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            df[col] = df[col].fillna(0)

    return df


# 5. Remove invalid rows
# What: Delete rows where price or quantity is negative.
# Why: Negative sales amounts are data-entry mistakes and corrupt analysis.

def remove_invalid_rows(df):
    """Remove rows with negative price or quantity values."""
    df = df.copy()

    if "price" in df.columns:
        df = df[df["price"] >= 0]
    if "quantity" in df.columns:
        df = df[df["quantity"] >= 0]

    return df



# Run the full cleaning pipeline

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load the raw data
    df_raw = load_data(raw_path)

    # Apply cleaning steps
    df_clean = clean_column_names(df_raw)
    df_clean = strip_whitespace(df_clean)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)

    # Save cleaned dataset
    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())
