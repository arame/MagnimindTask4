class gl:
    pkl_df_text = "pkl_df_text.pkl"
    pkl_df_edInput = "pkl_df_edInput.pkl"
    pkl_X_tfidf = "pkl_X_tfidf.pkl"
    pkl_X_bigram_tfidf = "pkl_X_bigram_tfidf.pkl"
    pkl_X_trigram_tfidf = "pkl_X_trigram_tfidf.pkl"
    pkl_X_stem_tfidf = "pkl_X_stem_tfidf.pkl"
    pkl_X_lem_tfidf = "pkl_X_lem_tfidf.pkl"
    pkl_classifier_LR = "pkl_classifier_LR.pkl"
    pkl_classifier_balanced_LR = "pkl_classifier_balanced_LR.pkl"
    pkl_classifier_SVM = "pkl_classifier_SVM.pkl"
    pkl_classifier_balanced_SVM = "pkl_classifier_balanced_SVM.pkl"
    pkl_multinomialclassifier_NBayes = "pkl_multinomialclassifier_NBayes.pkl"
    pkl_complementclassifier_NBayes = "pkl_complementclassifier_NBayes.pkl"
    # column names: ['tweetID', 'crDate','edInput', 'editor', 'engages', 'isApproved', 'isEdNeed', 'isRT', 'likes', 'photoUrl', 'retweets', 'rtUsID', 'text', 'topicName', 'usFlwrs', 'usID', 'usName', 'videoUrl']
    columns_not_needed = ['tweetID', 'crDate','edInput', 'editor', 'engages', 'isApproved', 'isEdNeed', 'isRT', 'likes', 'photoUrl', 'retweets', 'rtUsID', 'usFlwrs', 'videoUrl']
    text = "text"
    topic = "topicName"
    edInput = "edInput"
    is_business = "IsBusiness"
    usID = "usID"
    usName = "usName"
    output_folders = ["Pickle"]

