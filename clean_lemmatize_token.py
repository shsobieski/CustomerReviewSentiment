def clean_lemmatize_token(tweet):
    cleaned_tweet = re.sub(r"""['/,.;@#?!&$]+\ *""", " ", tweet, flags= re.VERBOSE).lower()
    tokenized_tweet = word_tokenize(cleaned_tweet)
    lemmatizer = WordNetLemmatizer()
    lemmatized_tweet = []
    for word in tokenized_tweet:
        lemmatized_tweet.append(lemmatizer.lemmatize(word))
    return lemmatized_tweet
