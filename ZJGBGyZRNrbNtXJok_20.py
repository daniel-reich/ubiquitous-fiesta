
def nearest_vowel(s):
    lst = [abs(ord(x)-ord(s)) for x in 'aeiou']
    return 'aeiou'[lst.index(min(lst))]

