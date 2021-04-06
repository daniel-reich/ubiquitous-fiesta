
def bw_transform(text):
  A=[text[i:]+text[:i] for i in range(len(text))]
  B=sorted(A)
  C=[x[-1] for x in B]
  return ''.join(C)

