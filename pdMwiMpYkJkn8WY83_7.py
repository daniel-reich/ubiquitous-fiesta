
def is_palindrome(word):
    x = len(word) // 2
    return word[:x] == word[::-1][:x]

