
def is_palindrome_possible(txt):
  return sum(txt.count(i)%2 for i in set(txt)) <= 1

