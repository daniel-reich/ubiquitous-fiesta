
def find_the_difference(s, t):
  return chr(sum(map(ord, t))-sum(map(ord, s)))

