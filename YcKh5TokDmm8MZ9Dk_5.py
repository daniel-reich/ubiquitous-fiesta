
import re
​
def hidden_anagram(txt, phrase):
    txt = re.sub('[^a-zA-Z]', '', txt.lower())
    phrase = sorted(re.sub('[^a-zA-Z]', '', phrase.lower()))
​
    for i in range(len(txt) - len(phrase) + 1):
        group = txt[i:i+len(phrase)]
        if sorted(group) == phrase:
            return group
    return 'noutfond'

