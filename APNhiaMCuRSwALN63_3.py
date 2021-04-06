
def almost_palindrome(txt):
    return len([1 for ch1, ch2 in zip(txt, txt[::-1])
                if ch1 != ch2]) == 2

