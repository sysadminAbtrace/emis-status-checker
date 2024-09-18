# Usage
  1. Place your old.csv and new.csv files in the same directory as this script.
  2. Run the script:

```python compare_csv.py```

# Functionality
  1. Load CSV Files: The script loads old.csv and new.csv into pandas DataFrames.
  2. Find New Items: It identifies new items in new.csv that are not present in old.csv based on the odscode column.
  3. Find Changed Lines: It finds lines where the isactivated status has changed from 0 to 1.

# Output
The script prints two sets of results:

  1. New items in new.csv that are not in old.csv:
        Displays the rows from new.csv that have odscode values not present in old.csv.

  2. Lines where isactivated changed from 0 to 1:
        Displays the rows from new.csv where the isactivated column changed from 0 in old.csv to 1 in new.csv.

