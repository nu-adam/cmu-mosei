from scripts import loader
from utils import dataset_operations as dsop, helpers

if __name__ == '__main__':
    '''
    To download the dataset, call loader.download_dataset() 
    and specify the modalities
    
    Here is a sample code for loading an existing dataset modality (highlevel),
    retrieving a sample size of one of its sequences (COVAREP) as a Python object,
    and storing it in a .json file
    '''

    cmumosei = loader.load_partial_dataset(
        'cmumosei/default/',
        50, # only first 50 videos are loaded (max possible is 3293)
        ['highlevel', 'labels']
    )
    cmumosei_highlevel = cmumosei['highlevel']
    