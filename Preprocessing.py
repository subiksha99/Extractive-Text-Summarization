from Obtaining_text import text
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from Generate_wordclouds import generate_wordcoud
import heapq

text = re.sub(r'\[[0-9]]*\]',' ', text)
text = re.sub(r'\s+',' ', text)

final_text = re.sub('[^a-zA-Z]',' ', text)
final_text = re.sub(r'\s+',' ', final_text)
generate_wordcoud(final_text)


list_of_sentences = nltk.sent_tokenize(text)

#Finding frequency of occurance of each word
stopwords = nltk.corpus.stopwords.words('english')
freq_of_words = {} # creating a dictionary
for word in nltk.word_tokenize(final_text):
    if word not in stopwords:
        if word not in freq_of_words.keys():
            freq_of_words[word] = 1
        else:
            freq_of_words[word] += 1

#print(freq_of_words)
#Finding the weighted frequency
max_freq = max(freq_of_words.values())
for word in freq_of_words.keys():
    freq_of_words[word] = (freq_of_words[word]/ max_freq)

#print(freq_of_words)

#Sentence scores using weighted frequencies calculated for each word
sentence_scores = {}
for sentence in list_of_sentences:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in freq_of_words.keys():
            if len(sentence.split(' ')) < 40:
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence] = freq_of_words[word]
                else:
                    sentence_scores[sentence] += freq_of_words[word]

summary = heapq.nlargest(7, sentence_scores, key = sentence_scores.get)

final_summary = ' '.join(summary)
print(final_summary)
