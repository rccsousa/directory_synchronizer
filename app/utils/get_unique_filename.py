import os

def get_unique_filename(base_filename: str) -> str:
    """
    Generate a unique filename by appending a number if the file already exists.
    """

    if not os.path.isfile(base_filename):
        return base_filename

    base, ext = os.path.splitext(base_filename)
    i = 1
    while True:
        new_filename = f"{base}({i}){ext}"
        if not os.path.isfile(new_filename):
            return new_filename
        i += 1
