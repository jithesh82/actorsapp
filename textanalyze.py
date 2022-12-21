# a python program to analyse speech
# to help actors with acting choices

import nltk
import random

# creating a list of words to be removed
stopw = nltk.corpus.stopwords.words('english')
# adding 'I' to the list
stopw.append('I')

#file = 'textguidepost.txt'
file = 'speak_the_speech.txt'

for line in  open(file): 
    #print(line)
    # breaking the line to word list
    words = nltk.word_tokenize(line)
    # removing punctuations
    words = [x for x in words if x.isalnum()]
    # removing stop words
    words = [x for x in words if x not in stopw]
    # printing words using random styles, foreground 
    # and background colors
    for word in words:
        style = random.randint(0,7)
        fg    = random.randint(31, 37)
        bg    = random.randint(40, 47)
        print(('\x1b[%s;%s;%sm' % (str(style), str(fg), str(40))) + word + '\x1b[0m', end=' ')
