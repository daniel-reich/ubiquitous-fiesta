
def first_n_vowels(txt, n):
    txt2 = ''
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
​
    for i in txt:
        if i in vowels:
            count += 1
            txt2 = txt2 + i
        if count == n:
            return txt2
    return 'invalid'

