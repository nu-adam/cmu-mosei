import os
from mmsdk import mmdatasdk

DEFAULT_PATH = '../cmumosei/'

def load_dataset(path, sources = ['raw', 'highlevel', 'labels']):
    # If the path directory does not exist, create it
    if not os.path.exists(path):
        print('The directory does not exist')
        return

    cmumosei_dataset = {}
    for s in sources:
        cmumosei_dataset[s] = mmdatasdk.mmdataset(f'{path}/{s}')
    return cmumosei_dataset

if __name__ == '__main__':
    # Loading the existing dataset from a directory
    load_dataset(DEFAULT_PATH, ['raw', 'highlevel', 'labels'])