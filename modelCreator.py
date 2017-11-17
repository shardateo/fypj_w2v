import scipy
import numpy
import matplotlib
import pandas
from gensim.models import Word2Vec
from nltk.tokenize import TweetTokenizer, word_tokenize

#list of punctuation/emoticons/special characters to remove from tweeter dataset
stopwords = ["?","d:","p:","::",":|",">:(","d: ","->","(;<",");","):<",".","..",".",";","^","__",",')",":-)",":'(",':-(',';)','`',"'",'(',')','!',":",",",'@',"..",'+',".",'[',']','"',"/","..",'…','?','...', '>', '<','~','#','&','-','___','=','*',":')",':(',':)',':/',':d',':p','<3','_','. . .', ';(', ';(','$','%','\\','):','|','(-:','(8','(:','(;','):','.','/:','0-0',"(':","(':","--->","(':",")':",")-:",'...','.',"}",'{',':\\']

#stopword removal method
def contains_word(s, w):
    return (' ' + w + ' ') in (' ' + s + ' ')


# define training data
sentences = []

file = open("files/particleDataset.txt", "r", encoding='utf8')
temp = file.read().splitlines()
tknzr = TweetTokenizer()

tweets = []
for i in temp:
	word_tokens = tknzr.tokenize(i.lower())
	filtered_tokens = []
	# print(word_tokens)
	# for stopword in stopwords:
	for tok, token in enumerate(word_tokens):
		word = word_tokens[tok]
		if word not in stopwords:
			# if word.find('#') <= -1:
			filtered_tokens.append(word)
	# print(filtered_tokens)
	tweets.append(filtered_tokens)
	print(len(tweets))
	# print(filtered_tokens)
file.close()

print("Tweets tokenized")




# train model
model = Word2Vec(tweets, min_count=3)

# summarize the loaded model
# print(model)
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
# print(model['and'])
# save model
model.save('singlish.bin3')
# load model
new_model = Word2Vec.load('singlish.bin3')
print(new_model)

# print(new_model.most_similar(positive=None, negative=None, topn=10, restrict_vocab=None, indexer=None))
print(new_model.similar_by_word('huh'))
