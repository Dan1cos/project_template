def console_output(string):
    """
    Function prints text to the console.

    Args:
        string (str): Text to be printed.

    Returns:
        None

    """
    print(string)


def file_output(path, data):
    """
    Function writes data to the file.

    Args:
        path (str): Path to the file.
        data: Any data to be written.

    Returns:
        None

    """
    with open(path, "a") as f:
        f.write(data)
        f.write("\n")
