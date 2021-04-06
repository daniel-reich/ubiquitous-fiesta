
def split(txt):
    vowels = []
    c = []
    for i in txt:
        if is_vowel(i):
            vowels.append(i)
        else:
            c.append(i)
    lst = vowels + c
    return "".join(lst)
            
​
​
def is_vowel(s):
    return s in ['a','e','i','o','u']

