
def get_vowel_substrings(txt):
    guide = [i for i in range(len(txt)) if txt[i] in 'aeiou']
    subs=[]
    for j in range(len(guide)):
        for k in range(j,len(guide)):
            subs.append(txt[guide[j]:guide[k]+1])
    return sorted(set(subs))
  
​
def get_consonant_substrings(txt):
    subs,guide = [], [i for i in range(len(txt)) if txt[i] not in 'aeiou']
    for j in range(len(guide)):
        for k in range(j,len(guide)):
            subs.append(txt[guide[j]:guide[k]+1])
    return sorted(set(subs))

