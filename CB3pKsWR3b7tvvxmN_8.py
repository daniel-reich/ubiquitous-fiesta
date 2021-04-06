
import re
def is_palindrome(txt):
    word1 = ''.join(re.findall("[a-zA-Z]+", txt)).lower()
    return word1 == word1[::-1]

