
def censor(s):
  vec = s.split(' ')
  cuv = ''
  for i in range(len(vec)):
    if len(vec[i]) <= 4:
      cuv = cuv + vec[i] + ' '
    else:
      for j in range(len(vec[i])):
        cuv = cuv + '*'
      cuv = cuv + ' '
  l = len(cuv)
  cuv = cuv[0:l-1]
  return cuv

