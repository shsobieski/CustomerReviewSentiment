def clean_lemmatize_token(tweet):
    stop_words = set(stopwords.words('english'))
    cleaned = tweet.translate(str.maketrans('', '', string.punctuation)).lower()
    tokenized = word_tokenize(cleaned)
    filtered = [w for w in tokenized if not w in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = []
    for word in filtered:
        lemmatized.append(lemmatizer.lemmatize(word))
<<<<<<< HEAD
    to_remove = ['rt','mention','sxsw','link']
=======
    for word in lemmatized:
        if word == '#':
            index = lemmatized.index('#')
            next_word = lemmatized[index + 1]
            joined = word + next_word
            list_to_remove = [next_word]
            lemmatized = [w for w in lemmatized if w not in list_to_remove]
            lemmatized.append(joined)
        else: 
            break
    to_remove = ['#']
>>>>>>> 230a864f5ad1f0c54851eaa68523bf7ca5a086f8
    lemmatized = [w for w in lemmatized if w not in to_remove]
    lemmatized = ' '.join(lemmatized)
    return lemmatized

