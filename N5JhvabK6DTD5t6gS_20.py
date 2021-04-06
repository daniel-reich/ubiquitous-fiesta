
import re
from string import punctuation
def markdown(symb):
    def encloser(match):
        return '{}{}{}'.format(symb, match.group(0), symb)    
    def replacer(s, word):
        regex = '{}[{}]*'.format(word, punctuation)
        return re.sub(regex, encloser, s, flags=re.IGNORECASE)
    return replacer

