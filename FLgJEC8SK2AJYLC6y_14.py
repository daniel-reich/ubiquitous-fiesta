
M = [ '12', '21', '2H', 'H2', 'H4', '4H', '43', '34']
​
​
def possible_path(lst):
  lst = list(map(str, lst))
​
  for move in map(lambda x: ''.join(x) , zip(lst[:], lst[1:])):
    if move not in M:
      return False
​
  return True

