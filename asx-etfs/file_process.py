import pandas as pd
from bs4 import BeautifulSoup

# Load the HTML file
with open('./page_source.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Define the expected headers (used for checking duplicates)
expected_headers = ["Exposure", "ASX Code", "Type", "iNAV", "Benchmark", "Investment Style", "Management Cost %", "Outperf' Fee", "Admission Date"]

# Find all rows in the table
rows = soup.find_all('tr')

# Extract data from each row
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    # Remove new lines within data fields to ensure proper formatting
    cols = [ele.replace('\n', ' ') for ele in cols]
    if len(cols) == 9:
        # Only append rows with the correct number of columns
        if cols != expected_headers:  # Check against repeating header rows
            data.append(cols)

# Create a DataFrame
df = pd.DataFrame(data, columns=expected_headers)

# Add the 'IsEnabled' column with default value '1'
df['IsEnabled'] = 1

# Save to CSV file
df.to_csv('./asx-etf.csv', index=False)

print("CSV file has been created successfully.")
