
def is_palindrome(txt) :
    for i in range(int((len(txt)/2))):
        if txt[i] == txt[len(txt)-i-1] :
            continue
        else:
            return False
    return True

