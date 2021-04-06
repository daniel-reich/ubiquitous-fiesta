
def is_palindrome(txt):
    from string import punctuation
    from re import sub
    txt_for = sub('[! ,-]', '', txt).lower()
    txt_rev = txt_for[::-1]
    return txt_for == txt_rev

