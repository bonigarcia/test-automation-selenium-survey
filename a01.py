import pandas as pd
import matplotlib.pyplot as plt

# Load the uploaded CSV file
file_path = "Test Automation with Selenium.csv"
df = pd.read_csv(file_path)

# Display basic information and the first few rows
# df.info(), df.head()

# Column containing experience data
experience_col = "How many years have you been working in the field of test automation?"

# Count non-null responses by category
experience_counts = df[experience_col].value_counts(dropna=False).sort_index()

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
ax.set_title("How many years have you been\nworking in the field of test automation?", fontsize=16)
fig.savefig("a01.pdf", bbox_inches='tight', pad_inches=0)
plt.show()