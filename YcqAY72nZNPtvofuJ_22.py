
def quad_sequence(lst):
  x, y, z = lst[-3:]
  delta = z - 2 * y + x
  diff = z - y
  seq = [z]
  
  for _ in range(len(lst)):
    diff += delta
    seq.append(seq[-1] + diff)
  
  return seq[1:]

