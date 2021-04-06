
import re
​
def find_longest(s):
    words = re.findall("\w+", s.lower())
    if not words[1:]:
        return words[0]
    remaining_words = find_longest(" ".join(words[1:]))
    return max(words[0], remaining_words, key = len)

