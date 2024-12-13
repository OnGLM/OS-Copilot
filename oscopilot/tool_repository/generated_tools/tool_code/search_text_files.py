def search_text_files(directory_path, keyword):
    """
    Search for all text files in the specified directory that contain the given keyword.

    Args:
    directory_path (str): The path of the directory to search for text files.
    keyword (str): The keyword to search for within the text files.

    Returns:
    list: A list of file paths that contain the specified keyword.
    """
    import os

    # Initialize a list to store file paths
    text_files = []

    # Iterate through all files in the directory
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if keyword in f.read():
                        text_files.append(file_path)

    return text_files