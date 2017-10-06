import nltk
print(nltk.__version__)

from nltk.corpus import gutenberg

print(gutenberg.fileids())

from nltk import FreqDist

fd = FreqDist(gutenberg.words('austen-persuasion.txt'))

print(fd.N())
print(fd.B())

samples = [item for item, _ in fd.most_common(10)]

for word, fq in fd.most_common(10):
    print(word, fq)
