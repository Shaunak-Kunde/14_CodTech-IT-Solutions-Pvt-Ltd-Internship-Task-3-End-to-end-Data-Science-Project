import pandas as pd

# Define the file paths
may_file_path = "C://Users//kunde//Desktop//Virtual internship//CodTech IT Solutions Pvt Ltd//CodTech IT Solutions Pvt Ltd Internship//Task-3 End to end Data Science Project//Goa Power Outage Report May 2025.xlsx"
june_file_path = "C://Users//kunde//Desktop//Virtual internship//CodTech IT Solutions Pvt Ltd//CodTech IT Solutions Pvt Ltd Internship//Task-3 End to end Data Science Project//Goa Power Outage Report June 2025.xlsx"

# Load the datasets
df_may = pd.read_excel(may_file_path)
df_june = pd.read_excel(june_file_path)

# Add a 'month' column and combine
df_may['month'] = 'May'
df_june['month'] = 'June'
df_combined = pd.concat([df_may, df_june], ignore_index=True)

# Correct the column name if needed
df_combined.rename(columns={'Feeder Name': 'Feeder_Name', 'Substation': 'Substation'}, inplace=True)

# Get unique values from the 'Substation' and 'Feeder Name' columns
unique_substations = df_combined['Substation'].unique().tolist()
unique_feeders = df_combined['Feeder Name'].unique().tolist()

print("--- Unique Substations ---")
for substation in unique_substations:
    print(substation)

print("\n--- Unique Feeder Names ---")
for feeder in unique_feeders:
    print(feeder)