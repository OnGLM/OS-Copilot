def list_text_files(directory_path):
    """
    List all text files in the specified directory.

    Args:
    directory_path (str): The path of the directory to list text files from.

    Returns:
    list: A list of file paths of text files in the specified directory.
    """
    import os

    # Initialize a list to store text file paths
    text_files = []

    # Iterate through all files in the directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                text_files.append(file_path)

    return text_files