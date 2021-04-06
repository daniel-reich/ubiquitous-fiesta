
import re
def replace_the(txt):
    words = txt.split()
    i = 0
    lst = []
    for ch in words:
        if ch == 'the' and re.match(r"^[aeiou]", words[i+1]):
            lst.append(ch.replace('the', 'an'))
            i += 1
        elif ch == 'the' and re.match(r"^[^aeiou]", words[i+1]):
            lst.append(ch.replace('the', 'a'))
            i += 1
        else:
            lst.append(ch)
            i += 1
    return " ".join(lst)

