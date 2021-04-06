
def is_palindrome(word):
    if word == "":
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1 : -1])
    return False

