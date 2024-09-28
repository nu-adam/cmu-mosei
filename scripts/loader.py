import os
from mmsdk import mmdatasdk
from utils import helpers, dataset_operations as dsop

DEFAULT_PATH = '../cmumosei/default/'
MODALITIES = {
    'raw': mmdatasdk.cmu_mosei.raw,
    'highlevel': mmdatasdk.cmu_mosei.highlevel,
    'labels': mmdatasdk.cmu_mosei.labels
}
DEFAULT_SOURCES = [key for key in MODALITIES]

# Download the dataset from scratch
def download_dataset(directory, sources = DEFAULT_SOURCES):
    helpers.ensure_directory(directory)
    
    cmumosei_dataset = {}
    for s in sources:
        cmumosei_dataset[s] = mmdatasdk.mmdataset(
            MODALITIES[s], f'{directory}/{s}'
        )
    return cmumosei_dataset

# Download an existing dataset
def load_dataset(directory, sources = DEFAULT_SOURCES):
    # If the path directory does not exist, create it
    if not os.path.exists(directory):
        print('This directory does not exist:', directory)
        return

    cmumosei = {}
    for s in sources:
        cmumosei[s] = mmdatasdk.mmdataset(f'{directory}/{s}')
    return cmumosei

def load_partial_dataset(directory, N, sources = DEFAULT_SOURCES):
    cmumosei = load_dataset(directory, sources)
    
    for modality in cmumosei.keys():
        cmumosei[modality] = dsop.retrieve_partial_dataset(
            cmumosei[modality], N
        )
    return cmumosei
    

if __name__ == '__main__':
    download_dataset(DEFAULT_PATH)