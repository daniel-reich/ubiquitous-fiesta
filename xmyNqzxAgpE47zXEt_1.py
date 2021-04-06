
import re
def is_alphabetically_sorted(sentence):
    match = re.findall("\w{3,}", sentence)
    return any(["".join(sorted(i.lower()))==i.lower() for i in match])

