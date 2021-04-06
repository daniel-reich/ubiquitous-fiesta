
def hangman(phrase, lst):
    ans = ''
    for x in phrase:
        if not x.isalpha():
            ans += x
        else:
            if x.lower() in lst:
                ans += x
            else:
                ans += '-'
    return ans

