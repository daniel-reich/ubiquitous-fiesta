
def letter_distance(t1, t2):
  return sum(abs(ord(i)-ord(j)) for i, j in zip(t1, t2)) + abs(len(t1)-len(t2))

