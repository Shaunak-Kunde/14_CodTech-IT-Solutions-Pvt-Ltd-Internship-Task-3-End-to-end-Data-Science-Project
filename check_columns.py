import pandas as pd

may_path = "C://Users//kunde//Desktop//Virtual internship//CodTech IT Solutions Pvt Ltd//CodTech IT Solutions Pvt Ltd Internship//Task-3 End to end Data Science Project//Goa Power Outage Report May 2025.xlsx"
june_path = "C://Users//kunde//Desktop//Virtual internship//CodTech IT Solutions Pvt Ltd//CodTech IT Solutions Pvt Ltd Internship//Task-3 End to end Data Science Project//Goa Power Outage Report June 2025.xlsx"

df_may = pd.read_excel(may_path)
df_june = pd.read_excel(june_path)
df_combined = pd.concat([df_may, df_june], ignore_index=True)

print("Combined DataFrame Columns:")
for col in df_combined.columns:
    print(f"'{col}'")