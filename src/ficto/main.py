import argparse
from datetime import datetime
import os

from ficto.core.generate import create_dataframe



def generate_file(dataconfig, numrows, filetype):
    """
    Generate a file based on data configuration.

    Parameters:
    - dataconfig (str): Path to the YAML file for data configuration.
    - numrows (int): Number of rows to generate.
    - filetype (str): Type of file to be generated (csv or json).

    Returns:
    None
    """
    # Create a dataframe using the provided data_config and num_rows
    df = create_dataframe(dataconfig, numrows)

    # Create a sub-folder named 'data' if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Generate the current time for the filename
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Shape of the dataframe
    shape_df = df.shape

    # Define the file path based on file_type
    file_path = f"data/{shape_df[0]}_{shape_df[1]}_{numrows}_{current_time}"

    # Save the dataframe to a file based on file_type
    if filetype == 'csv':
        file_path += '.csv'
        df.to_csv(file_path, index=False)
    elif filetype == 'json':
        file_path += '.json'
        df.to_json(file_path, orient='records')

    print(f"File saved at: {file_path}")


def main():
    """
    Main entry point of the script. Parses command line arguments and calls generate_file.
    (Ex: python main.py -d config.yaml -n 100 -f csv)
    """
    parser = argparse.ArgumentParser(description="Generate a file based on data configuration.")
    parser.add_argument('-d', '--dataconfig', required=True, help='Path to the YAML file for data configuration')
    parser.add_argument('-n', '--numrows', type=int, required=True, help='Number of rows')
    parser.add_argument('-f', '--filetype', choices=['csv', 'json'], required=True, help='Type of file to be generated (csv or json)')

    args = parser.parse_args()

    generate_file(dataconfig=args.dataconfig, numrows=args.numrows, filetype=args.filetype)

if __name__ == "__main__":
    main()
