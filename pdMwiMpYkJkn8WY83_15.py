
def is_palindrome(word):
    if word=='':
        return True
    else:
        if word[::-1]==word:
            return True
        else:
            return False

