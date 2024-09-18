import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('old.csv')
df2 = pd.read_csv('new.csv')

# Find new items in df2 that are not in df1 based on 'odscode'
new_items = df2[~df2['odscode'].isin(df1['odscode'])]

# Print the results
print("New items in 2.csv that are not in 1.csv:")
print(new_items)

# Ensure 'odscode' is the index for easy comparison
df1.set_index('odscode', inplace=True)
df2.set_index('odscode', inplace=True)

# Find lines where 'isactivated' changed from 0 to 1
changed_lines = df2[(df2['isactivated'] == 1) & (df1['isactivated'] == 0)]

# Reset index to make 'odscode' a column again
changed_lines.reset_index(inplace=True)

# Print the results
print()
print("Lines where 'isactivated' changed from 0 to 1:")
print(changed_lines)
