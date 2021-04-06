
def is_palindrome(p):
  meh = ''.join(l for l in p.lower() if l.isalpha())
  if len(meh)<2:
    return True
  return meh[0] == meh[-1] and is_palindrome(meh[1:-1])

