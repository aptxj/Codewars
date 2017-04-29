'''
Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''

###############
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

###############
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

################
import re

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

################

def pig_it(text):
	return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.IGNORECASE)

################

def pig_it(text):
	return re.sub(r'(\w)(\w*)', r'\g<2>\g<1>ay', text)

################

def pig_it(text):
    res = []

    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)

    return ' '.join(res)

##################

from string import punctuation
def pig_it(text):
    words = text.split(' ')
    return ' '.join(
        [
            '{}{}ay'.format(
                word[1:],
                word[0]
            ) if word not in punctuation else word for word in words
        ]
    )


####################

def pig_it(text):
    return __import__("re").sub(r'\b\w+\b', lambda m: m.group(0)[1:] + m.group(0)[0] + 'ay', text)

###################

import re
def pig_it(text):
  return re.sub(r'\w+', lambda m: m.group(0)[1:] + m.group(0)[0] + 'ay', text)

