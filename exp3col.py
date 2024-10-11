import pandas as pd

def extract_columns(csv_file, columns, output_file):
    """Imports a CSV file, extracts specified columns, and saves the result to a new CSV file."""

    df = pd.read_csv(csv_file)

    # Select the desired columns
    extracted_df = df[columns]

    # Save the extracted data to a new CSV file
    extracted_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    csv_file = "your_data.csv"  # Replace with your CSV file path
    columns_to_extract = ["Column1", "Column2", "Column3"]  # Replace with your column names
    output_file = "extracted_data.csv"

    extract_columns(csv_file, columns_to_extract, output_file)