import h5py

def raw_words_features_to_sentences(words_features):
    sentences = []
    text = ''
    for item in words_features:
        # words in words_dataset are encoded as bytes
        word = item[0].decode('utf-8')
        if word == 'sp':
            sentences.append(text)
            text = ''
        else: text += word + ' '
    return sentences

def raw_words_features_to_string(words_features):
    text = ''
    for item in words_features:
        # words in words_dataset are encoded as bytes
        word = item[0].decode('utf-8')
        if word == 'sp':
            text += '\n'
        else: text += word + ' '
    return text

def raw_words_to_intervaled_sentences(raw_words):
    # Sentences and intervals will be synced
    sentences = []
    intervals = []
    
    text = ''
    start_time = raw_words['intervals'][0][0].item() # numpy datatype to python datatype
    last_word_id = len(raw_words['features']) - 1
    # The number of features and intervals are assumed to be the same
    for i in range(last_word_id):
        # Words in words_dataset are encoded as bytes
        word = raw_words['features'][i][0].decode('utf-8')
        if word == 'sp':
            # Recording the end_time of the interval
            # end_time corresponds to the end time of the last word in the sentence
            end_time = raw_words['intervals'][i][1].item()
            intervals.append([start_time, end_time])
            if i < last_word_id:
                # Resetting start_time of the next sentence
                start_time = raw_words['intervals'][i + 1][0].item()
            
            sentences.append(text)
            text = ''
        else: text += word + ' '

    return {
        'sentences': sentences, 
        'intervals': intervals
    }