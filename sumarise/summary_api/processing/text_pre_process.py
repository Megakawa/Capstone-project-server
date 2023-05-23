from pyvi import ViTokenizer
from gensim.models import KeyedVectors
import regex
import numpy as np
import nltk
nltk.download('punkt')

def clean_text(text):

    text = regex.sub("(?s)<ref>.+?</ref>", "", text) # remove reference links
    text = regex.sub("(?s)<[^>]+>", "", text) # remove html tags
    text = regex.sub("&[a-z]+;", "", text) # remove html entities
    text = regex.sub("(?s){{.+?}}", "", text) # remove markup tags
    text = regex.sub("(?s){.+?}", "", text) # remove markup tags
    text = regex.sub("(?s)\[\[([^]]+\|)", "", text) # remove link target strings
    text = regex.sub("(?s)\[\[([^]]+\:.+?]])", "", text) # remove media links
    text = regex.sub("[']{5}", "", text) # remove italic+bold symbols
#    text = regex.sub(u"[^ \r\n\p{Latin}\-'‘’.?!]", " ", text)
    text = text.lower()
    text = regex.sub("[ ]{2,}", " ", text) # Squeeze spaces.
    return text

def sentence_segment(text):

    sents = nltk.sent_tokenize(text)
    return sents

def word_segment(sent):

    words = ViTokenizer.tokenize(sent).split()
    return words

def create_sentence(text):
    contents_parsed = clean_text(text)
    sentences = sentence_segment(contents_parsed)
    return sentences

def create_sentences_embedding(text):
    w2v = KeyedVectors.load("/home/hungpromax11/Capstone-project-server/sumarise/summary_api/processing/gensim-model.model")
    vocab = w2v.wv.index_to_key
    X = []
    sentences = create_sentence(text)
    for sentence in sentences:
        if sentence is not None:
            words = word_segment(sentence)
            sentence_vec = np.zeros((100))
            for word in words:
                if word in vocab:
                    sentence_vec+=w2v.wv[word]
            X.append(sentence_vec)
    return X, len(sentences), sentences
