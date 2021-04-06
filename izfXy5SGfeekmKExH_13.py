
def puzzle_pieces(a1, a2):
  if len(a1) == len(a2):
    a3 = [a1[x] + a2[x] for x in range(len(a2))]
    check = a1[0] + a2[0]
    if a3.count(check) == len(a1):
      return True
    else:
      return False
  else:
    return False

