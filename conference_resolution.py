import spacy
import neuralcoref

"""
    Input:  A text paragraph.
    Return type: List containing endorphic aware resolution of the sentences
    in the paragraph.
"""

def conference_resolve(text):
    nlp = spacy.load('en')
    neuralcoref.add_to_pipe(nlp)
    doc1 = nlp(text)
    return doc1._.coref_clusters

if __name__=='__main__':
    print(conference_resolve('My sister has a dog. She loves him.'))