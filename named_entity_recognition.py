import spacy
from spacy import displacy
from pathlib import Path

"""
    Input:  A list of sentences.
    Return type: A list of list of named entities and their labels in each sentence. 
"""
def ner_recognizer(sentences):
    nlp = spacy.load("en_core_web_sm")
    ner_sentences=[]
    for sentence in sentences:
        doc = nlp(sentence)
        ners = []
        for ent in doc.ents:
            ners.append([ent.text,ent.label_])
        ner_sentences.append(ners)
    i=1
    for sentence in sentences:
        doc = nlp(sentence)
        svg = displacy.render(doc, style="ent")
        file_name = "sentence_"+str(i)+".html"
        output_path = Path("./ner/" + file_name)
        output_path.open("w", encoding="utf-8").write(svg)
        i+=1
    return ner_sentences

if __name__=='__main__':
    print(ner_recognizer(["Saurabh makes 1000 dollars."]))