"""
This module is used to coordinate the pipeline
"""
import sentence_segmentation as sen_seg 
import tokenization as tk
import pos_tagger as pt
import lemmatization as lt
import stop_words as sw
import dependency_parsing as dp
import noun_phrases as np
import named_entity_recognition as ner
import conference_resolution as cer

def get_text():
    file = open('source_text.txt','r')
    text = file.read()
    return text

def segment_sentence(text):
    sentences = sen_seg.segment(text)

    print("\n\nPipeline step 1: Segmenting sentences:\n\n")
    i=1
    for sentence in sentences:
        print("Sentence "+str(i)+": "+sentence+"\n")
        i+=1
    return sentences

def tokenize_sentence(sentences):
    tokens = tk.tokenize(sentences)
    print("\n\nPipeline step 2: Tokenizing Sentence:\n\n")
    i=1
    for token in tokens:
        print("Sentence "+str(i)+" Tokens: ")
        print(token,end="\n")
        i+=1
    return tokens

def parts_of_speech_tagging(tokens):
    
    print("\n\nPipeline step 3: POS Tagging:\n\n")
    pos_tags = pt.pos_tagging(tokens)
    i=1
    for tags in pos_tags:
        print("POS Tagged Sentence "+str(i)+": ")
        print(tags,end="\n")
        i+=1

def lemmatize(tokens):
    print("\n\nPipeline step 4: Lemmatization:\n\n")
    lemmatized_list = lt.lemmatize_tokens(tokens)
    i=1
    for sentence in lemmatized_list:
        print("Lemmatized Sentence "+str(i)+": ")
        print(sentence,end="\n")
        i+=1

def stop_words_removal(tokens):
    
    print("\n\nPipeline step 5: Removing Stop Words from the Sentence:\n\n")
    no_sw_sentences = sw.remove_stop_words(tokens)
    i=1
    for sentence in no_sw_sentences:
        print("Sentence "+str(i)+" without stopwords :")
        print(sentence,end="\n")
        i+=1

def parse_dependency(sentences):
    print("\n\nPipeline step 6: Parsing dependency for each Sentence:\n\n")
    dp.dependency_parsing(sentences)

def noun_phrase_extraction(sentences):
    nouns_list = np.noun_phrase(sentences)

    print("\n\nPipeline step 7: Noun Phrases for the Sentences:\n\n")
    i=1
    for sentence in sentences:
        print("Sentence "+str(i)+" :")
        print(sentence,end="\n")
        print("Noun phrases:")
        print(nouns_list[i-1],end="\n")
        i+=1

def named_entity_recognition(sentences):
    entities = ner.ner_recognizer(sentences)
    print("\n\nPipeline step 8: Named Entity Recognition for the Sentences:\n\n")
    i=1
    for sentence in sentences:
        print("Sentence "+str(i)+" :")
        print(sentence,end="\n")
        print("Named Entity Recognition:")
        print(entities[i-1],end="\n")
        i+=1

def conference_resolution(text):
    print("\n\nPipeline step 9: Conference Resolution:\n\n")

    conf_list = cer.conference_resolve(text)

    for key in conf_list:
        print(key)

text = get_text()
print("NLP PIPELINE:\n\n")
print("Orignial text:\n")
print(text)
sentences = segment_sentence(text)
tokens = tokenize_sentence(sentences)
parts_of_speech_tagging(tokens)
lemmatize(tokens)
stop_words_removal(tokens)
parse_dependency(sentences)
noun_phrase_extraction(sentences)
named_entity_recognition(sentences)
conference_resolution(text)