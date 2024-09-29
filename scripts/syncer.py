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
            print(modality, seq, len(vids))
    print('----------------------------------------------------------------')
    
    return

    for modality in cmumosei.keys():
        loader.deploy_dataset_modality(cmumosei[modality], f'cmumosei/custom_10_aligned/{modality}')