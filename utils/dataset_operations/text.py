import h5py

def raw_words_features_to_string(words_features):
    text = ''
    for item in words_features:
        # words in words_dataset are encoded as bytes
        word = item[0].decode('utf-8')
        if word == 'sp': text += '\n'
        else: text += word + ' '
    return text