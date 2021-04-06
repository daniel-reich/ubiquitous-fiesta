
def word_to_decimal(word):
    letters, word = "abcdefghijklmnopqrstuvwxyz", word.lower()
    bs, ln = letters.index(max(word))+11, len(word)-1
    return sum((letters.index(ch)+10) * bs**(ln-i) for i,ch in enumerate(word))

