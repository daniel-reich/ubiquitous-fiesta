
def min_palindrome_steps(txt):
  return len(txt) - max((len(txt[i:]) for i in range(0, len(txt)) if is_palindrome(txt[i:])) or [1])
  
  
def is_palindrome(w):
  return w == w[::-1]

