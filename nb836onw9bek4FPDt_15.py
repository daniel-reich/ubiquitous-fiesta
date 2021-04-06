
import re
​
​
def count_same_ends(txt):
    remove_punct = re.sub(r"[^ A-Za-z]", "", txt)
    count = 0
    for word in remove_punct.lower().split():
        if len(word) > 1:
            if word[0] == word[-1]:
                count += 1
    return count

