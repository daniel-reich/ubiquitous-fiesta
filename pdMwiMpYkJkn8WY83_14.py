
def is_palindrome(word):
    # base case
    if len(word) == 0:
        return True
​
    # recursion case
    else:
        if word[0] == word[-1]:
            word = word[1:-1]
            return is_palindrome(word)
​
    return False

