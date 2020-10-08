
from nltk.corpus import stopwords

"""
    Input:  A list of tokens.
    Return type: List containing sentences from the tokens without stop words. 
"""

def remove_stop_words(tokens_list):
    stop_words = set(stopwords.words('english'))
    sentence_list_without_stop_words = []
    for tokens in tokens_list:
        tokens_without_stopwords = []
        for token in tokens:
            if token not in stop_words:
                tokens_without_stopwords.append(token)
        filtered_sentence = " ".join(tokens_without_stopwords)
        sentence_list_without_stop_words.append(filtered_sentence)
    return sentence_list_without_stop_words
