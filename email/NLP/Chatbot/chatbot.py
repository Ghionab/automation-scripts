import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import wikipedia


text = wikipedia.page("Vegetables").content

lemmatizer=WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

def process(text, question):
    sentence_tokens = nltk.sent_tokenize(text)
    sentence_tokens.append(question)

    tv = TfidfVectorizer(tokenizer=lemma_me)

    tf = tv.fit_transform(sentence_tokens)

    cosine_sim = cosine_similarity(tf[-1], tf)

    index=cosine_sim.argsort()[0][-2]

    values_flat=cosine_sim.flatten()
    values_flat.sort()
    print(values_flat)

    coff=values_flat[-2]
    print(coff)
    if coff>0.3:
      return sentence_tokens[index]
      
while True:
    question = input("Ask me a question: ")
    output=process(text, question)
    if question == 'exit':
        break
    elif output:
        print(output)
    else:
        print("I don't know the answer to that question.")