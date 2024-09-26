import pandas as pd
import numpy as np
import argparse
from tabulate import tabulate

def read_and_clean_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    pd.set_option('future.no_silent_downcasting', True)
    # Replace '\N' with NaN
    df.replace('\\N', np.nan, inplace=True)

    # Drop columns where all values are NaN
    # df.dropna(axis=1, how='all', inplace=True)

    return df

def dataframe_to_markdown(df):
    # Convert DataFrame to Markdown using tabulate
    markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)
    return markdown_table


def main():
    """
    Main function to parse arguments and process the CSV file.
    """
    parser = argparse.ArgumentParser(description='Convert CSV file to Markdown')
    parser.add_argument('file_path', type=str, help='Path to the CSV file')
    args = parser.parse_args()

    df = read_and_clean_csv(args.file_path)
    markdown_output = dataframe_to_markdown(df)
    print(markdown_output)

if __name__ == "__main__":
    main()
