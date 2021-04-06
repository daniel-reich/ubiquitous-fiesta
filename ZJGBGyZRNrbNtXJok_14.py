
def nearest_vowel(s):
    dic = {"a" : 97, "e" : 101, "i" : 105, "o" : 111, "u" : 117 }
    look = ord(s)
    off = [(abs(dic[key] - look), key) for key in dic]
    return min(off)[1]

