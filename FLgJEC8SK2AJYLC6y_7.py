
from re import match
def possible_path(lst):
  lst = [72 if i == 'H' else i for i in lst]
  return all(abs(a - b) == 1 or a == 72 and bool(match(r'[24]', str(b))) or bool(match(r'[24]', str(a))) and b == 72 for a, b in zip(lst[0:-1], lst[1:]))

