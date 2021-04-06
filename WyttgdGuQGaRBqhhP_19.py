
def min_palindrome_steps(s):
    st = 0
    i, j = 0, len(s)-1
    while i <= j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            j = len(s) -1
            st += 1
            i = st
    return st

