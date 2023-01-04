class gl:
    pkl_df_text = "pkl_df_text.pkl"
    pkl_df_is_business = "pkl_df_is_business.pkl"
    pkl_X_tfidf = "pkl_X_tfidf.pkl"
    pkl_classifier_LR = "pkl_classifier_LR.pkl"
    pkl_classifier_SVM = "pkl_classifier_SVM.pkl"
    # column names: ['tweetID', 'crDate','edInput', 'editor', 'engages', 'isApproved', 'isEdNeed', 'isRT', 'likes', 'photoUrl', 'retweets', 'rtUsID', 'text', 'topicName', 'usFlwrs', 'usID', 'usName', 'videoUrl']
    columns_not_needed = ['tweetID', 'crDate','edInput', 'editor', 'engages', 'isApproved', 'isEdNeed', 'isRT', 'likes', 'photoUrl', 'retweets', 'rtUsID', 'usFlwrs', 'videoUrl']
    text = "text"
    topic = "topicName"
    is_business = "IsBusiness"
    sourceId = "usID"
    source = "usName"
    output_folders = ["Pickle"]

