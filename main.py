from scripts import loader
from utils import printers, dataset_operations as dsop
from pprint import pprint

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
        50, # first 50 videos are loaded (max possible is 3293)
        ['raw', 'highlevel', 'labels']
    )
    words = cmumosei['raw']['words']
    keys = list(words.keys())
    intervaled_sentences = dsop.text.raw_words_to_intervaled_sentences(words[keys[2]])
    pprint(intervaled_sentences)