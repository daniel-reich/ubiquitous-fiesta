
def replace_vowel(word):
    vowel={"a":1,"e":2,"i":3,"o":4,"u":5}
    return "".join([str(i) if i not in  vowel else str(vowel[i]) for i in word])

