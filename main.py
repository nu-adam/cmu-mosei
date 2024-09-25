from scripts import loader
from utils import dataset_operations as dsop
from pprint import pprint

if __name__ == '__main__':
    cmumosei_highlevel = loader.load_dataset(
        'cmumosei/default/', ['highlevel']
    )['highlevel']
    highlevel_partial = dsop.retrieve_partial_sequence(cmumosei_highlevel['COVAREP'], 2)
    dsop.sequence_to_json_file(highlevel_partial, 'cmumosei/custom/covarep_2.json')