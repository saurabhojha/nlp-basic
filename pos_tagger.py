import nltk

"""
    Input:  A list of list of tokens.
    Return type: List of list of tuples where every token is tagged. 
"""

def pos_tagging(tokens):
    tagged_list = []
    for token in tokens:
        tagged_list.append(nltk.pos_tag(token))
    return tagged_list