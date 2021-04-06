
def is_palindrome(wrd):
    if len(wrd) >= 2:
        return False if wrd[0] != wrd[-1] else is_palindrome(wrd[1:-1])
    else:
        return True

