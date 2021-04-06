
def max_separator(txt):
    separators = [letter for letter in set(txt) if txt.count(letter) >= 2]
    words = []
    for i in range(len(txt)):
        if txt[i] in separators and txt[i:].count(txt[i]) >= 2:
            words.append(txt[i:(txt.find(txt[i],i+1) + 1)])
    return sorted([i[0] for i in words if len(i) == len(max(words,key = len))])

