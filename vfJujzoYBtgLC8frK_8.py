
def word_to_decimal(word):
    word = word.lower()
    base = 10 + max([ord(c) - 96 for c in word])
    ans = 0
    power = 1
    for c in word[::-1]:
        ans += power * (ord(c) - 97 + 10)
        power *= base
    return ans

