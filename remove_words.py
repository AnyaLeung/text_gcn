from nltk.corpus import stopwords
import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
import sys
from utils import clean_blank_line

dataset = 'out'
nltk.download('stopwords')

# Read Word Vectors
# word_vector_file = 'data/glove.6B/glove.6B.200d.txt'
# vocab, embd, word_vector_map = loadWord2Vec(word_vector_file)
# word_embeddings_dim = len(embd[0])
# dataset = '20ng'

doc_content_list = []
word_freq = {}  # to remove rare words

f = open('data/corpus/'+dataset+'.txt', 'rb')
for text in f.readlines():
    doc_content_list.append(text.strip().decode('utf8'))
f.close()

for doc_content in doc_content_list:
    words = doc_content.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

print(word_freq)

clean_docs = []
for doc_content in doc_content_list:
    words = doc_content.split()
    doc_words = []
    for word in words:
        if word_freq[word] >= 5:
            doc_words.append(word)
    doc_str = ' '.join(doc_words).strip()
    clean_docs.append(doc_str)

clean_corpus_str = '\n'.join(clean_docs)
#print(clean_corpus_str)

f = open('data/corpus/'+dataset+'_clean.txt', 'w')
f.write(clean_corpus_str)
f.close()

clean_blank_line('data/corpus/'+dataset+'_clean', 
        'data/corpus/'+dataset+'_clean_without_blankline')


min_len = 10000
aver_len = 0
max_len = 0 

f = open('data/corpus/'+dataset+'_clean_without_blankline.txt', 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    temp = line.split()
    aver_len = aver_len + len(temp)
    if len(temp) < min_len:
        min_len = len(temp)
    if len(temp) > max_len:
        max_len = len(temp)
f.close()
aver_len = 1.0 * aver_len / len(lines)
print('min_len : ' + str(min_len))
print('max_len : ' + str(max_len))
print('average_len : ' + str(aver_len))
