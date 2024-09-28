import h5py

def pretty_print_hdf5_group(hdf5_group, indent=0):
    """
    Recursively prints the structure of an HDF5 group in a readable way.
    """
    # Loop through each item in the group
    for key in hdf5_group:
        item = hdf5_group[key]

        # Indentation for pretty output
        space = '    ' * indent
        print(f"{space}- {key}:", end=" ")

        # Check if it's a dataset
        if isinstance(item, h5py.Dataset):
            # Get dataset information
            print(f"Dataset, shape: {item.shape}, dtype: {item.dtype}")
            # Print the dataset values
            print(f"{space}  Data: {item[:]}")  # Access dataset contents
        
        # Check if it's a group (subgroup)
        elif isinstance(item, h5py.Group):
            print(f"Group:")
            # Recursively print the subgroup contents
            pretty_print_hdf5_group(item, indent + 1)