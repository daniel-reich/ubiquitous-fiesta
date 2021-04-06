
def same_vowel_group(w):
    ans = [w[0]]
    vowels = get_vowels(w[0])
    for x in w[1:]:
        if get_vowels(x) == vowels:
            ans.append(x)
    return ans
    
def get_vowels(word):
    sov = set()
    for x in word:
        if x in 'aeiou':
            sov.add(x)
    return sov

