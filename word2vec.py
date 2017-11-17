import scipy
import numpy
import matplotlib
import pandas
from gensim.models import Word2Vec

new_model = Word2Vec.load('models/singlish2.bin')
print(new_model.similar_by_word('huh'))


