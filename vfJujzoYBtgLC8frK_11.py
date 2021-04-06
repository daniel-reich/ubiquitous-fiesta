
def word_to_decimal(word):
    word = word.lower()
    base = ord(max(word))-86
    l = len(word)
    return sum((ord(word[i])-87) * (base**(l-i-1)) for i in range(l))

