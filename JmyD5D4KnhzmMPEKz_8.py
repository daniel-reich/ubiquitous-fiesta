
import re
​
def constraint(txt):
    txt = txt.lower()
    chars = re.sub(r"[^a-zA-Z]", "", txt)
    count = 0
    words = txt.split()
    print(words)
    check = set(words[0])
    for num in range(1, len(words)):
        if len(check & set(words[num])) > 0:
            count += 1
    if len(set(chars)) == 26:
        return "Pangram"
    elif len(set(chars)) == len(chars):
        return "Heterogram"
    elif all(ch[0] == txt[0] for ch in words):
        return "Tautogram"
    elif count == len(words) - 1:
        return "Transgram"
    else:
        return "Sentence"

