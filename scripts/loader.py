import os
from mmsdk import mmdatasdk
from utils import helpers

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

    cmumosei_dataset = {}
    for s in sources:
        cmumosei_dataset[s] = mmdatasdk.mmdataset(f'{directory}/{s}')
    return cmumosei_dataset