
def min_palindrome_steps(txt):
    if txt == txt[::-1]:
        return 0
    for x in range(len(txt)-2,-1,-1):
        if txt[x] == txt[-1]:
            return x
    return len(txt) - 1

