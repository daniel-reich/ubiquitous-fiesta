
import re
​
def most_common_words(text, n):
    text = re.findall('\w+', text.lower())
    groups = [(i, text.count(i)) for i in set(text)]
    return dict(sorted(groups, key=lambda x: (-x[1], text.index(x[0])))[:n])

