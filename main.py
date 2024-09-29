from scripts import loader, syncer
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
        5, # first 50 videos are loaded (max possible is 3293)
        ['raw', 'highlevel', 'labels']
    )
    words = cmumosei['raw']['words']
    keys = list(words.keys())
    intervaled_sentences = dsop.text.raw_words_to_intervaled_sentences(words[keys[2]])
    # pprint(intervaled_sentences['intervals'])
    labels = dsop.comp_sequence_to_dictionary(cmumosei['labels']['All Labels'])
    # pprint(labels[keys[2]]['intervals'])
    labeled_sentences = syncer.sync_sentences_with_labels(intervaled_sentences, labels[keys[2]])
    pprint(labeled_sentences)