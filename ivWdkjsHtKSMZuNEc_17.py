
import re
​
def find_shortest_words(txt):
    chars = sorted(re.sub(r"[^a-z\s]", "", txt.lower()).split(" "))
    min_length = min([len(n) for n in chars if n.isalpha()])
    return [m for m in chars if len(m) == min_length]

