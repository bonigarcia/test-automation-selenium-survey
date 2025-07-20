import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
file_path = "Test Automation with Selenium.csv"
df = pd.read_csv(file_path)

# Column
col = "How do you manage the browser drivers?"

# Count non-null responses by category
experience_counts = df[col].value_counts(dropna=False).sort_index()

# Plot pie chart
fig, ax = plt.subplots(figsize=(7, 7))
#fig, ax = plt.subplots()

# Customize font size for labels and percentages
wedges, texts, autotexts = ax.pie(
    experience_counts,
    labels=experience_counts.index,
    autopct='%1.1f%%',
    textprops={'fontsize': 12}  # Label and percentage font size
)

# Set title with specific font size
ax.set_title(col, fontsize=16)

# Save and show chart
plt.savefig("b04.pdf", dpi=300, bbox_inches='tight', pad_inches=0) 
plt.tight_layout()
plt.show()