import spacy
from spacy import displacy
from pathlib import Path

"""
    Input:  A list of sentences.
    Return type: Saves a dependency diagram for each sentence. 
"""

def dependency_parsing(sentences):
    nlp = spacy.load("en_core_web_sm")
    i=1
    for sent in sentences:
        doc = nlp(sent)
        svg = displacy.render(doc, style="dep", jupyter=False)
        file_name = "sentence_"+str(i)+".svg"
        output_path = Path("./images/" + file_name)
        output_path.open("w", encoding="utf-8").write(svg)
        i+=1

if __name__=='__main__':
    dependency_parsing(["SKo is the best"])