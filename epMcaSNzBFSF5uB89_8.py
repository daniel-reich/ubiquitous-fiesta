
def currently_winning(scores):
  y = [scores[i] for i in range(len(scores)) if i%2==0]
  o = [scores[i] for i in range(len(scores)) if i%2!=0]
  ys=0
  os=0
  ret = []
  for i in range(len(y)):
    ys+=y[i]
    os+=o[i]
    ret.append('Y') if ys>os else ret.append('O') if os>ys else ret.append('T')
  return ret

