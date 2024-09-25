import os
from mmsdk import mmdatasdk

DEFAULT_PATH = '../cmumosei/'
MODALITIES = {
    'raw': mmdatasdk.cmu_mosei.raw,
    'highlevel': mmdatasdk.cmu_mosei.highlevel,
    'labels': mmdatasdk.cmu_mosei.labels
}

def download_dataset(path, sources = ['raw', 'highlevel', 'labels']):
    # If the path directory does not exist, create it
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'Folder created: {path}')
    
    cmumosei_dataset = {}
    for s in sources:
        cmumosei_dataset[s] = mmdatasdk.mmdataset(
            MODALITIES[s], f'{path}/{s}'
        )
    return cmumosei_dataset

if __name__ == '__main__':
    # Downloading the dataset to a directory
    download_dataset(DEFAULT_PATH, ['raw', 'highlevel', 'labels'])