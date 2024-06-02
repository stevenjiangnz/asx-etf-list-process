import os
import pandas as pd
import html

def combine_csv_files(directory, output_file):
    # List all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    combined_df = pd.DataFrame()
    
    for file in csv_files:
        file_path = os.path.join(directory, file)
        # Read each CSV file
        df = pd.read_csv(file_path)
        
        # Remove asterisks from the 'EXCHANGE' column
        df['EXCHANGE'] = df['EXCHANGE'].str.replace('*', '')
        
        # Decode HTML entities in the dataframe
        # Convert each column to string before applying html.unescape
        for col in df.columns:
            df[col] = df[col].astype(str).apply(html.unescape)
        
        # Filter out rows where 'CURRENCY' is not 'USD'
        df = df[df['CURRENCY'] == 'USD']
        
        # Concatenate data into one DataFrame
        combined_df = pd.concat([combined_df, df])
    
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv(os.path.join(directory, output_file), index=False)
    print(f"Combined file created: {output_file}")

# Specify the directory containing the CSV files
directory = './us-etfs/raw/'
# Name of the output file
output_file = 'combined_us_etf.csv'

combine_csv_files(directory, output_file)
