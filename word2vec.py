import scipy
import numpy
import matplotlib
import pandas
from gensim.models import Word2Vec

new_model = Word2Vec.load('models/singlish3.bin')

#reading discourse particles to be queried
file = open("files/particles.txt", "r", encoding='utf8')
temp = file.read().splitlines()

particles = []
for i in temp:
    particles.append(i)
file.close()
print("Particles loaded")

# print(new_model.similar_by_word('kill')[0][0])
# print(len(new_model.similar_by_word('kill')))

file = open("output/w2vres.txt", "w", encoding='utf8')
for particle in particles:
    vectorRes = []
    for data in range(len(new_model.similar_by_word(particle))):
        vectorRes.append(new_model.similar_by_word(particle)[data][0])
    sentence= ""
    for index,val in enumerate(vectorRes):
        if index == 0:
            sentence = val
        else:
            sentence=sentence+","+val
    file.writelines(particle + " = [" + sentence + "]\n")
file.close()

file = open("output/w2vres.txt", "r", encoding='utf8')
temp = file.read().splitlines()

particles = []
for i in temp:
    particles.append(i)
file.close()

file = open("output/w2vres.txt", "w", encoding='utf8')
particles = sorted(particles)
for particle in particles:
    file.writelines(particle + "\n")
file.close()