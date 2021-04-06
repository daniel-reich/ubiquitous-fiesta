
def get_vowel_substrings(txt):
    myans = []
    v = ['a','e','i','o','u']
    for i in range(len(txt)):
        if txt[i] in v:
            for j in range(i,len(txt)):
                if txt[j] in v:
                    if txt[i:j+1] not in myans:
                        myans.append(txt[i:j+1])
    return sorted(myans)
​
def get_consonant_substrings(txt):
    myans = []
    v = ['a','e','i','o','u']
    for i in range(len(txt)):
        if txt[i] not in v:
            for j in range(i,len(txt)):
                if txt[j] not in v:
                    if txt[i:j+1] not in myans:
                        myans.append(txt[i:j+1])
    return sorted(myans)

