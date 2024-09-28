import os
import json
import random

def ensure_directory(path):
    directory = os.path.dirname(path)
    
    # Only create directory if it exists (non-empty)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def save_as_json_file(item, filepath):
    ensure_directory(filepath)

    with open(filepath, 'w') as f:
        json.dump(item, f, indent=4)
        
def delete_rand_items(items, n):
    to_delete = set(random.sample(range(len(items)), n))
    return [x for i, x in enumerate(items) if not i in to_delete]