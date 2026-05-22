from crewai.tools import tool

@tool("read_local_file")
def read_local_file(file_path: str) -> str:
    """Useful for reading the content of a local text file on the machine."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"
