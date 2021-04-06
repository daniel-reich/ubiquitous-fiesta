
def is_palindrome(wrd):
    if wrd[0] != wrd[-1]: return False
    elif len(wrd) == 1: return True 
    return is_palindrome(wrd[1:-1])

