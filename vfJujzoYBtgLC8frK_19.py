
def word_to_decimal(word):
    word = word.lower()
    base = ord(max(word)) - 86
    ans = [int(i,base) * base ** j for j,i in enumerate(word[::-1])]
    return sum(ans)

