
from math import floor
import string
def polybius(text):
    # Anonymous Functions
    get_row = lambda idx, width=5: str(1+floor(idx/width))
    get_column = lambda idx,width=5: str(1+idx % 5)
​
    # Create cypher dictionary
    cypher = {}
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split(' ')
​
    for idx,letter in enumerate(letters):
        if idx > 8:
            idx -= 1  # Down shift to account for I/J sharing
        if letter != 'j':
            row = get_row(idx)
            col = get_column(idx)
            rc = int(row+col)
            cypher[letter] = rc
            cypher[rc] = letter
        else:
            row = get_row(8) # letter i is index 8
            col = get_column(8)
            rc = int(row+col)
            cypher[letter] = rc
            cypher[rc] = 'i'
​
        
​
​
    # Determine if message x is encrypted already
    try:
        _ = int(text.split()[0])
        encrypted = True
    except ValueError:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        encrypted = False
​
​
    if encrypted:
        result = ''
        for term in text.split(' '):
            word = ''
            for i in range(int(len(term)/2)):
                key = int(term[i*2:i*2+2])
                word += cypher[key]
            result += word
            result += ' '
    else:
        result = ''
        for word in text.split(' '):
            term = ''
            for letter in word:
                term += str(cypher[letter])
            result += '{} '.format(term)
​
​
    return result[:-1]

