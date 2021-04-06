
def is_magic(square):
  if not square:
    return True
  if any([any([i<1 or i>len(square)**2 for i in j]) for j in square]):
    return False
  s = sum(square[0])
  col = [[i[j] for i in square] for j in range(len(square))]
  rd = sum([square[i][i] for i in range(len(square))])
  ld = sum([square[i][-i-1] for i in range(len(square))])
  return all([sum(i)==s for i in square]) and all([sum(i)==s for i in col]) and rd==s and ld==s

