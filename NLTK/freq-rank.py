from nltk.corpus import gutenberg
from nltk import FreqDist

import matplotlib
import matplotlib.pyplot as plt

fd = FreqDist()

for text in gutenberg.fileids():
    print(text,end=' ')
    for word in gutenberg.words(text):
        fd[word] += 1
    print("......done")


samples = fd.most_common()

freqs = [freq for _, freq in samples]
ranks = [i for i in range(1, fd.B() + 1)]
# print(freqs)
# print(ranks)

plt.loglog(ranks, freqs)
plt.xlabel('requency(f)', fontsize = 14, fontweight = 'bold')
plt.ylabel('rank(r)', fontsize = 14, fontweight = 'bold')
plt.grid(True)
plt.show()
