
import re
​
def is_parsel_tongue(sentence):
    return len(re.findall('[sS]{2,}', sentence)) == len([i for i in sentence.lower().split() if 's' in i])

