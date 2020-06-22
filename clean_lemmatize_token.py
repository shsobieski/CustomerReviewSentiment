def clean_lemmatize_token(tweet):
    stop_words = set(stopwords.words('english'))
    cleaned_tweet = tweet.translate(str.maketrans('', '', string.punctuation)).lower()
    tokenized_tweet = word_tokenize(cleaned_tweet)
    filtered_tweet = [w for w in tokenized_tweet if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tweet = []
    for word in filtered_tweet:
        lemmatized_tweet.append(lemmatizer.lemmatize(word))
    return lemmatized_tweet

