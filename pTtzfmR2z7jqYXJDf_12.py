
def possible_palindrome(txt):
  s = [txt.count(x) for x  in set(txt)]
  return sum(x % 2 > 0 for x  in s) < 2

