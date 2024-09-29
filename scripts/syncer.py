def sync_sentences_with_labels(intervaled_sentences, emotion_labels):
    sentences = intervaled_sentences['sentences']
    intervals = intervaled_sentences['intervals']
    
    # Helper function to calculate overlap between two intervals
    def get_overlap(interval1, interval2):
        start1, end1 = interval1
        start2, end2 = interval2
        overlap = max(0, min(end1, end2) - max(start1, start2))
        return overlap

    results = []
    
    for sentence_idx, sentence_interval in enumerate(intervals):
        sentence_start, sentence_end = sentence_interval
        sentence_duration = sentence_end - sentence_start
        
        # List to store the weighted contributions for this sentence
        weighted_emotions = [0.0] * 7  # 7 emotions, all initialized to 0
        contributing_labels = []  # Store contributing emotional labels
        
        total_overlap = 0  # To track total overlap time with emotional intervals
        
        # Check against each emotion label interval
        for emotion_idx, emotion_interval in enumerate(emotion_labels['intervals']):
            overlap_duration = get_overlap(sentence_interval, emotion_interval)
            
            if overlap_duration > 0:
                # There is an overlap, calculate the overlap ratio
                overlap_ratio = overlap_duration / sentence_duration
                total_overlap += overlap_duration
                
                # Get the emotional features for the current emotion interval
                emotion_features = emotion_labels['features'][emotion_idx]
                
                # Add weighted contribution of each emotion to the sentence's emotion
                for i in range(7):  # There are 7 emotions
                    weighted_emotions[i] += emotion_features[i] * overlap_ratio
                
                # Append the contributing label if there is an overlap
                contributing_labels.append(emotion_features)
        
        # Finalize result entry
        if total_overlap > 0:
            final_label = weighted_emotions
        else:
            final_label = None
        
        # Append the result for this sentence
        result = {
            'sentence': sentences[sentence_idx],
            'interval': sentence_interval,
            'final_label': final_label,
            'adjacent_labels': contributing_labels if total_overlap > 0 else []
        }
        
        results.append(result)
    
    return results

def default_sync(cmumosei):
    print('Before alignment')
    for modality in cmumosei.keys():
        for seq in cmumosei[modality].keys():
            vids = [vid for vid in cmumosei[modality][seq].keys()]
            print(modality, seq, len(vids))
    print('----------------------------------------------------------------')
    
    cmumosei['highlevel'].align('glove_vectors')
    print('After aliging by glove_vectors')
    for modality in cmumosei.keys():
        for seq in cmumosei[modality].keys():
            vids = [vid for vid in cmumosei[modality][seq].keys()]
            print(modality, seq, len(vids))
    print('----------------------------------------------------------------')

    cmumosei['highlevel'].impute('glove_vectors')
    print('After imputing')
    for modality in cmumosei.keys():
        for seq in cmumosei[modality].keys():
            vids = [vid for vid in cmumosei[modality][seq].keys()]
            print(modality, seq, len(vids))
    print('----------------------------------------------------------------')
    
    cmumosei['highlevel'].computational_sequences['All Labels'] = cmumosei['labels']['All Labels']
    cmumosei['highlevel'].align('All Labels')
    print('After aligning by All Labels')
    for modality in cmumosei.keys():
        for seq in cmumosei[modality].keys():
            vids = [vid for vid in cmumosei[modality][seq].keys()]
            print(modality, seq, len(vids))
    print('----------------------------------------------------------------')
    
    cmumosei['highlevel'].hard_unify()
    print('After hard unification')
    for modality in cmumosei.keys():
        for seq in cmumosei[modality].keys():
            vids = [vid for vid in cmumosei[modality][seq].keys()]
            print(modality, seq, vids)
    print('----------------------------------------------------------------')
    
    return

    for modality in cmumosei.keys():
        loader.deploy_dataset_modality(cmumosei[modality], f'cmumosei/custom_10_aligned/{modality}')