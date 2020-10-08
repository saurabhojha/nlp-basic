import spacy

"""
    Input:  A list of sentences.
    Return type: A list of list of noun phrases in each sentence. 
"""

def noun_phrase(sentences):
    nlp = spacy.load("en_core_web_sm")
    noun_phrase_list =[]
    for sentence in sentences:
        doc = nlp(sentence)
        nouns = []
        for chunk in doc.noun_chunks:
            nouns.append(chunk.text)
        noun_phrase_list.append(nouns)
    return noun_phrase_list    

if __name__=='__main__':
    print(noun_phrase(["Saurabh is good"]))