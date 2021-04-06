
import re
​
def syllable_count(s):
    syllables = 0
    for i in re.findall("[a-z']+", s, re.I):
        groups = len(re.findall('[aeiouy]+', i, re.I))
        syllables += max(1, groups - 1 if i.endswith(('e', 'es', "e's", 'ed')) and not i.endswith('le') else groups)
    return syllables
​
def haiku(s):
    return list(map(syllable_count, s.split('/'))) == [5, 7, 5]

