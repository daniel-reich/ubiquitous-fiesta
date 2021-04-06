
import re
def is_parsel_tongue(sentence):
    if re.search('ss', sentence.lower()) and all(word.lower().count('s') != 1 for word in sentence.split()):
        return True
    return False

