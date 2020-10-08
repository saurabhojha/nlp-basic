from nltk.tokenize import word_tokenize as wt

"""
    Input:  A list of sentences
    Return type: List of List containing tokens in each sentences. 
"""
def tokenize(sentences):
    tokens = []

    for sentence in sentences:
        tokens.append(wt(sentence))
    return tokens