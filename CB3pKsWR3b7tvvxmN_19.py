
def is_palindrome(txt):
    txt = txt.lower()
    txt = ''.join([x for x in txt if x.isalpha()])
    if txt == txt[::-1]:
        return True
    else:
        return False

