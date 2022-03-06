# a python program to analyse speech
# to help actors with acting choices

import nltk
import random

stopw = nltk.corpus.stopwords.words('english')
stopw.append('I')

#file = 'textguidepost.txt'
file = 'speak_the_speech.txt'

for line in  open(file): 
    #print(line)
    words = nltk.word_tokenize(line)
    words = [x for x in words if x.isalnum()]
    words = [x for x in words if x not in stopw]
    for word in words:
        #import time
        #random.seed(time.time())
        style = random.randint(0,7)
        fg    = random.randint(31, 37)
        bg    = random.randint(40, 47)
        print(('\x1b[%s;%s;%sm' % (str(style), str(fg), str(40))) + word + '\x1b[0m', end=' ')
    #print('\x1b[0m')
    #print(words)
    #break
