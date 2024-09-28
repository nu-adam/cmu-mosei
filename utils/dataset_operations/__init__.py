from . import text

from utils import helpers

def retrieve_partial_dataset(dataset, N = 50, random = False):
    seq_ids = list(dataset.keys())
    # All sequences are assumed to have the same set of video IDs
    all_video_ids = list(dataset[seq_ids[0]].keys())
    if N > len(all_video_ids):
        raise ValueError(f'N has to be no more than {len(all_video_ids)}')
    
    # We need only N amount of videos
    # So we get rid of the rest
    to_remove = []
    if random:
        # Identifying which videos to remove
        to_remove = helpers.delete_rand_items(all_video_ids, N)
    else:
        # To remove everything except the first N amount
        to_remove = all_video_ids[N:]
    
    for vid in to_remove:
        dataset.remove_id(vid)
    return dataset

def hdf5_sequence_to_dictionary(comp_sequence):
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
    
    return sequence_obj