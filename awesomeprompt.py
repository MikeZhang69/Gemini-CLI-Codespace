import pandas as pd
# Read the CSV file
df = pd.read_csv("hf://datasets/fka/awesome-chatgpt-prompts/prompts.csv")
# Save to Excel file
df.to_excel("prompts.xlsx", index=False)