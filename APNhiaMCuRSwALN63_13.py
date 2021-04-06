
def almost_palindrome(txt):    
    return len([ch for index, ch in enumerate(txt) if txt[index] != txt[::-1][index]]) == 2

