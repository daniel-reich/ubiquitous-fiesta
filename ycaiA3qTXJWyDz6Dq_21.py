
import re
​
​
def consonants(word):
    return len(re.findall('[^(a|e|i|o|u| |\W|\d)]', word, re.I))
​
​
def vowels(word):
    return len(re.findall('(a|e|i|o|u)', word, re.I))

