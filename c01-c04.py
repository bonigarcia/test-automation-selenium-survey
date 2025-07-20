import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("Test Automation with Selenium.csv")

# Target issues
issues_to_plot = ["Assertability", "Asynchrony", "Brittleness", "Failure analysis"]

# Response label mapping
label_map = {
    1: "Fully disagree",
    2: "Disagree",
    3: "Not sure",
    4: "Agree",
    5: "Fully agree"
}

# Setup subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs = axs.flatten()

# Create a bar chart for each issue
for i, issue in enumerate(issues_to_plot):
    # Calculate percentage distribution
    value_counts = df[issue].value_counts(normalize=True).reindex([1, 2, 3, 4, 5], fill_value=0) * 100
    labels = [label_map[k] for k in value_counts.index]

    # Plot bar chart
    axs[i].bar(labels, value_counts.values, color='cornflowerblue')
    axs[i].set_title(issue)
    axs[i].set_ylim(0, 40)
    axs[i].set_ylabel("Responses (%)")
    axs[i].tick_params(axis='x', rotation=45)

# Save and show chart
fig.savefig("c01-04.pdf", bbox_inches='tight', pad_inches=0)
plt.tight_layout()
plt.show()