
def is_palindrome(p):
  if len(p) <2:
    return True
  elif not p.isalpha():
    newP = ''
    for _,char in enumerate(p):
      if char.isalpha():
        newP += char
    return is_palindrome(newP.lower())
  else:
    first = p[0];last = p[-1]
    return first.lower() == last.lower() and is_palindrome(p[1:-1])

