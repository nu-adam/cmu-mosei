import os

def ensure_directory(path):
    directory = os.path.dirname(path)
    
    # Only create directory if it exists (non-empty)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

