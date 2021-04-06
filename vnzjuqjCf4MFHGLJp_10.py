
def shift_letters(txt, n):
    letters = [c for c in txt if c.isalpha()]
    l = len(letters)
    n %= l
    letters = letters[-n:] + letters[:-n]
    ans = ""
    for c in txt:
        if c.isalpha():
            ans += letters.pop(0)
        else:
            ans += c
    return ans

