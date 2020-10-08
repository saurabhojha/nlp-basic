from nltk.stem import WordNetLemmatizer

"""
    Input:  A list of tokens.
    Return type: List containing lemmatized sentences from the tokens. 
"""

def lemmatize_tokens(tokens_list):
    lemmatizer = WordNetLemmatizer()
    lemmatized_list = []
    for tokens in tokens_list:
        lemmatized_sentence = ''
        for token in tokens:
            lemmatized_sentence+= lemmatizer.lemmatize(token,pos = "v") + ' '
        lemmatized_list.append(lemmatized_sentence) 
    return lemmatized_list

