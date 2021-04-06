
def is_palindrome(txt):
  return ''.join(i for i in txt.lower() if i.isalpha()) == ''.join(i for i in txt.lower() if i.isalpha())[::-1]

