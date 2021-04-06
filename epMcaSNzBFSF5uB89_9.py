
def currently_winning(scores):
  yc = [scores[0]]
  oc = [scores[1]]
  for i in range(2, len(scores)):
    if i % 2 == 0:
      yc.append(scores[i] + yc[-1])
    else:
      oc.append(scores[i] + oc[-1])
  x = []
  for i in range(len(yc)):
    if yc[i] == oc[i]:
      x.append('T')
    elif yc[i] > oc[i]:
      x.append('Y')
    else:
      x.append('O')
  return x

