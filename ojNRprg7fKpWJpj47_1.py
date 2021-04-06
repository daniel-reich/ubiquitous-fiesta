
def shift_sentence(txt):
  a = txt.split()
  return" ".join(a[i-1][0]+a[i][1:] for i in range(len(a)))

