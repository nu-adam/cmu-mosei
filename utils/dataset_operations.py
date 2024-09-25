import json
from pprint import pprint
from utils import helpers

def retrieve_partial_sequence(comp_sequence, N = 50):
    all_video_ids = list(comp_sequence.data.keys())
    selected_video_ids = all_video_ids[:N]
    partial_dataset = {vid: comp_sequence.data[vid] for vid in selected_video_ids}
    
    return partial_dataset

def sequence_to_json_file(comp_sequence, filepath = 'sequence.json'):
    helpers.ensure_directory(filepath)
    
    sequence_obj = {}
    for vid in comp_sequence.keys():
        video_obj = {
            'features': list(),
            'intervals': list()
        }
        for member in comp_sequence[vid].keys():
            # the members are always 'features' and 'intervals'
            # it is how CMU-MOSEI is structured
            for row in comp_sequence[vid][member]:
                video_obj[member].append(row.tolist())
        sequence_obj[vid] = video_obj

    with open(filepath, 'w') as f:
        json.dump(sequence_obj, f, indent=4)