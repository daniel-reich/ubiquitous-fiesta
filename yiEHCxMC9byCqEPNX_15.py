
def is_palindrome(p):
    result = ''
    for char in p:
        if char.isalpha():
              result += char.lower()
    if len(result) <=1:
           return True
    else:
        if result[0] == result[-1]:
                   return is_palindrome(result[1:-1])
        return False

