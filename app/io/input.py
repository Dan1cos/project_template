import pandas as pd


def console_input():
    """
    Function triggers text input from the console.

    Returns:
        str: Inputted text from the console.

    """
    return input("Enter text: ")


def file_input(path):
    """
    Function reads content from the file.

    Args:
        path (str): Path to the file.

    Returns:
        str: Inputted file content read by python.

    """
    with open(path, "r") as f:
        return f.read()


def pandas_input(path):
    """
    Function reads content from the file using pandas.

    Args:
        path (str): Path to the file.

    Returns:
        pandas.DataFrame: Inputted file content read by pandas.

    """
    return pd.read_csv(path)
