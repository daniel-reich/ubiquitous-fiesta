
def high_low(txt):
  lst = [int(i) for i in txt.split(' ')]
  return str(max(lst)) + ' ' + str(min(lst))

