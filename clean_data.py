import pandas as pd
import re

def clean_healthcare_data(input_csv, output_csv="cleaned_data.csv"):
    # Load the CSV file
    df = pd.read_csv(input_csv)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Handle missing values (fill with 'Unknown' or drop)
    df.fillna("Unknown", inplace=True)

    # Standardize column names (lowercase, replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Standardize text columns (remove special characters, convert to lowercase)
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].str.lower().str.replace(r'[^a-z0-9 ]', '', regex=True)

    # Convert date columns to a standard format (if any)
    date_columns = ["dob", "admission_date", "discharge_date"]  # Update based on your dataset
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')

    # Save the cleaned data
    df.to_csv(output_csv, index=False)
    print(f"✅ Data cleansing complete! Cleaned data saved as {output_csv}")

# Example usage
if __name__ == "__main__":
    input_file = "raw_healthcare_data.csv"  # Update with actual input file
    clean_healthcare_data(input_file)
