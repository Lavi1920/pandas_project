# %load q03_get_run_counts/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import pandas as pd
# You have been given the dataset already in 'ipl_df'.
df = read_csv_data_to_df('./data/ipl_dataset.csv')

# Solution
count=0
def get_run_counts():
    series = pd.Series(df['runs']+count)
    return series

get_run_counts()




