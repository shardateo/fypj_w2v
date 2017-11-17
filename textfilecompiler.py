#reading discourse particles to be queried
file = open("files/particles.txt", "r", encoding='utf8')
temp = file.read().splitlines()

particles = []
for i in temp:
    particles.append(i)
file.close()

file2 = open("files/particleDataset.txt","w",encoding='utf8')
for particle in particles:
    file = open("particleHits//" + particle + ".txt","r",encoding='utf8')
    temp = file.read().splitlines()
    for tweets in temp:
        file2.writelines(tweets + '\n')

    file.close()

file2.close()


