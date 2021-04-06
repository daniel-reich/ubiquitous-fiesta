
def possible_palindrome(txt):
  return sum(txt.count(i)%2 for i in set(txt)) <= 1

