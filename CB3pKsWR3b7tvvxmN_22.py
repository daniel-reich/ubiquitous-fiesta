
def is_palindrome(txt):
  return ''.join([ch.lower() for ch in txt if ch.isalpha()]) == ''.join([ch.lower() for ch in txt if ch.isalpha()])[::-1]

