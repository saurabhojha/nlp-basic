from nltk.tokenize import sent_tokenize as st 

"""
    Input:  A text paragraph.
    Return type: List containing sentences in the paragraph. 
"""

def segment(text):
    return st(text)