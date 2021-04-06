
def puzzle_pieces(a1, a2):
  print(a1)
  print(a2)
  out = True
  val = 0
  temp = []
  if len(a1) != len(a2):
    out = False
  else:
    for i in range(0, len(a1)):
      val = a1[i]+a2[i]
      temp.append(val)
      print(temp)
      if len(set(temp)) == 1:
        continue
      else:
        out = False
        break
  return out

