
import re
​
def char_appears(sentence, char):
​
    words = re.findall(r'\w+', sentence)
​
    return [word.lower().count(char) for word in words]

