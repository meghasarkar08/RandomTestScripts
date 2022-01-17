import os
import pandas as pd

# Provide paths for base path for CSV file and CSV filename
BASE_DIR = r'C:\Users\megha\Documents\Python Programming\Input Testdata'
FILE_CSV = '\CSV\data-1.csv'

# User should create a Parquet folder from base path
# A parameter is set to Parquet path
FILE_PATH_PARQUET = BASE_DIR + r'\PARQUET'

# Extract the CSV file and split to the exact filename without extension so that
# the parquet file name is similar to the exact csv
CSV_FILE = BASE_DIR + FILE_CSV
filename = os.path.basename(CSV_FILE)

split_tup = os.path.splitext(filename)
PARQUET_FILE = FILE_PATH_PARQUET + '\\' + split_tup[0] + '.parquet'


def write_parquet_file():
    df = pd.read_csv(CSV_FILE)
    df.to_parquet(PARQUET_FILE)


write_parquet_file()

df = pd.read_parquet(PARQUET_FILE)
print(df)
