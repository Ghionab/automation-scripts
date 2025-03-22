import nltk
# nltk.download("punkt_tab")
#nltk.download('averaged_perceptron_tagger_eng')

from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

#print(sentence_tokens)


#print(pos_tag)

def lemma(sentence):
    sentences=[]
    sentence_tokens=nltk.word_tokenize(sentence.lower())
    pos_tag=nltk.pos_tag(sentence_tokens)
    print(pos_tag)
    
    for token,pos_tag in zip(sentence_tokens, pos_tag):
        if  pos_tag[1][0].lower() in ["n", "v","r", "a"]:
           lemma=lemmatizer.lemmatize(token, pos_tag[1][0].lower())
           print(lemma)
           sentences.append(lemma)
        else:
           sentences.append(sentence_tokens)
    return sentences

x=lemma("I am of learning python")
print(x)