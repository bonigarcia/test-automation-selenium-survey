import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("Test Automation with Selenium.csv")

# Identify relevant columns
unit_testing_columns = [col for col in df.columns if 'unit testing framework' in col.lower()]
language_column = [col for col in df.columns if 'primary programming language' in col.lower() and '[orig]' not in col][0]

# Subset the dataframe
df_unit_testing = df[[language_column] + unit_testing_columns]

# Reshape for analysis
melted_df = df_unit_testing.melt(
    id_vars=language_column,
    var_name="Unit Testing Framework",
    value_name="Usage"
)

# Filter to keep only meaningful usage entries
active_usage = melted_df[melted_df["Usage"].isin(["Always", "Often"])].copy()

# Clean framework names for readability
active_usage["Unit Testing Framework"] = active_usage["Unit Testing Framework"].str.extract(r'\[(.*?)\]')

# Group by language and framework
language_framework_counts = (
    active_usage.groupby(
        [language_column, "Unit Testing Framework"]
    ).size().unstack(fill_value=0)
)

# Generate distinct colors using a qualitative colormap
num_frameworks = len(language_framework_counts.columns)
cmap = plt.colormaps.get_cmap('tab20')
colors = [cmap(i) for i in range(num_frameworks)]

# Plot the stacked bar chart
language_framework_counts.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 7),
    title="Usage of Unit Testing Frameworks by Programming Language",
    color=colors
)

# Improve plot aesthetics
plt.xlabel("Programming Language")
plt.ylabel("Number of Mentions")
plt.xticks(rotation=45)

# Save and show chart
plt.savefig("b08.pdf", dpi=300, bbox_inches='tight', pad_inches=0) 
plt.tight_layout()
plt.show()