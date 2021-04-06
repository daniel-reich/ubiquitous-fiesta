
def is_palindrome_possible(txt):
  sets = set(txt)
  num_values = {x: txt.count(x) for x in sets}
  values = [x % 2 for x in num_values.values()]
  return values.count(1) <= 1

