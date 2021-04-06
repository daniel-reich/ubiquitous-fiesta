
def dif_ciph(inpt):
  if type(inpt)==str:
    a = list(map(ord,inpt))
    return [a[0]] + [a[i]-a[i-1] for i in range(1,len(a))]
  a = [inpt[0]]
  [a.append(i+a[-1]) for i in inpt[1:]]
  return "".join(map(chr,a))

