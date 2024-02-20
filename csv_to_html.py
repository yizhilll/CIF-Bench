import pandas as pd

# Load the CSV file
csv_file = 'leaderboard.csv'  # Change this to the path of your CSV file
df = pd.read_csv(csv_file)

# Convert the DataFrame to HTML
html_table = df.to_html(index=False)

# Add CSS to make the table scrollable
scrollable_table_style = """
<style>
    .scrollable-table {
        overflow-y: auto;
        height: 400px; /* Adjust the height as needed */
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th, td {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    th {
        background-color: #f2f2f2;
    }
</style>
"""

# Wrap the table in a div that makes it scrollable
scrollable_table_html = f"""
{scrollable_table_style}
<div class="scrollable-table">
    {html_table}
</div>
"""

# Save the HTML to a file
html_file = 'tmp.html'  # Change this to your desired output HTML file path
with open(html_file, 'w') as file:
    file.write(scrollable_table_html)

print(f"HTML table saved to {html_file}")

