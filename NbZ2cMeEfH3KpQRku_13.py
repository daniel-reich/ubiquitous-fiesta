
def portion_happy(n):
  unhappy = sum(x != y and x == z for x, y ,z in zip(n[:-2], n[1:-1], n[2:]))
  edge = (n[0] != n[1]) + (n[-1] != n[-2])
  return (len(n) - (unhappy + edge)) / len(n)

