
def print_all_groups():
  lst =  ["a", "b", "c", "d", "e"]
  r = ''
  for n in range(1, 7):
    for ch in lst:
      if ch == 'e' and n == 6:
        break
      r += str(n) + ch + ', '
  r += '6e'
  return r

