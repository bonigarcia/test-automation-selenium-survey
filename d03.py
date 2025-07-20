import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "Test Automation with Selenium.csv"
df = pd.read_csv(file_path)

# Filter columns
col_name = "Which AI-assisted tools have you used for test automation?"
cols = [col for col in df.columns if col.startswith(col_name)]

# Define the Likert scale mapping
pd.set_option('future.no_silent_downcasting', True)
likert_map = {"Never": 1, "Rarely": 2, "Sometimes": 3, "Often": 4, "Always": 5}

# Replace Likert responses with numeric scores
df = df[cols].replace(likert_map)

# Calculate average and median scores for each use case
average_scores = df.mean()
median_scores = df.median()

# Create a DataFrame to hold both
importance_data = pd.DataFrame({
    'Average': average_scores,
    'Median': median_scores
})

# Shorten column labels for better chart readability
short_labels = {
    col: col.replace(col_name + " [", "").replace("]", "")
    for col in cols
}
importance_data.index = importance_data.index.to_series().replace(short_labels)

# Sort by average
importance_data_sorted = importance_data.sort_values(by='Average', ascending=False)

# Set bar colors based on average score
def assign_color(avg):
    if round(avg,2) >= 4.3:
        return '#8dcfaf'  # Dark green
    elif round(avg,2) >= 3.6:
        return '#b6dfc5'  # Green
    elif round(avg,2) >= 3:
        return '#f4faf8'  # Light green
    elif round(avg,2) >= 2.3:
        return '#fdf2f2'  # Light red
    elif round(avg,2) >= 1.6:
        return '#f4c5c0'  # Red
    else:
        return '#eb988e'  # Dark red

# Assign colors to each bar
colors = [assign_color(avg) for avg in importance_data_sorted['Average']]

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(importance_data_sorted.index, importance_data_sorted['Average'], color=colors, edgecolor='black')

# Add median labels to bars
for i, (avg, med) in enumerate(zip(importance_data_sorted['Average'], importance_data_sorted['Median'])):
    ax.text(avg + 0.05, i, f"{round(avg,2)}", va='center', ha='left', fontsize=10)

# Style the chart
ax.set_xlabel("Average Importance Score\n(1=Never, 2=Rarely, 3=Sometimes, 4=Often, 5=Always)")
ax.set_title("AI-Powered Tools by Perceived Importance")
ax.invert_yaxis()

# Save and show chart
plt.xlim(1, 5)
plt.savefig("d03.pdf", dpi=300, bbox_inches='tight', pad_inches=0) 
plt.tight_layout()
plt.show()