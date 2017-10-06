from nltk.corpus import gutenberg
from nltk import ConditionalFreqDist
from random import choice

cfd = ConditionalFreqDist()

prev_word = None

for word in gutenberg.words("austen-persuasion.txt"):
    cfd[prev_word][word] += 1
    prev_word = word

word = 'therefore'
i = 1

for i in range(1, 20):
    print(word,end=' ')
    lwords = list(set(cfd[word]))
    # print(lwords)
    follower = choice(lwords)
    word = follower
