
def three_sum(li):
  l = len(li)
  meh = [[li[i],li[j],li[k]] for i in range(l) for j in range(l) for k in range(l) if i<j<k and li[i]+li[j]+li[k]==0]
  return [meh[i] for i in range(len(meh)) if meh[i] not in meh[:i]]

