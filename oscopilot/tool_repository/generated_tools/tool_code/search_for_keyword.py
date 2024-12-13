def search_for_keyword(text_files, keyword):
    """
    Search for the specified keyword in the given list of text files.

    Args:
    text_files (list): A list of file paths to search within.
    keyword (str): The keyword to search for in the text files.

    Returns:
    list: A list of file paths that contain the specified keyword.
    """
    # Initialize a list to store file paths that contain the keyword
    matching_files = []

    # Iterate through each file in the list
    for file_path in text_files:
        try:
            # Open the file and read its content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # Check if the keyword is present in the file content
                if keyword in content:
                    matching_files.append(file_path)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    return matching_files