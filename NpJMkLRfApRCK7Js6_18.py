
def is_palindrome(wrd):
    if len(wrd) in (0, 1):
        return True
    return (wrd[0] == wrd[-1] and
             is_palindrome(wrd[1:len(wrd)-1]))

