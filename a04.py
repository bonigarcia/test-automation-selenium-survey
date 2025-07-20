import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the CSV file
file_path = "Test Automation with Selenium.csv"
df = pd.read_csv(file_path)

# Column
col = "Where do you work?"
work_entries = df[col].dropna()

# Split entries by semicolon and normalize them
split_entries = work_entries.str.split(";").explode().str.strip()

# Classify values into Academia, Industry, or Other
classified = split_entries.apply(lambda x: x if x in ["Academia", "Industry"] else "Other")

# Count the values and compute percentages
counts = Counter(classified)
total = sum(counts.values())
percentages = {k: v / total * 100 for k, v in counts.items()}

# Plot pie chart
fig, ax = plt.subplots(figsize=(7, 7))
plt.pie(percentages.values(), labels=percentages.keys(), autopct='%1.1f%%', textprops={'fontsize': 12})
ax.set_title(col, fontsize=16)
plt.show()
fig.savefig("a04.pdf", bbox_inches='tight', pad_inches=0)

