
def dial(txt):
  d={'abc'  : '2',
  'def'  : '3',
  'ghi'  : '4',
  'jkl'  : '5',
  'mno'  : '6',
  'pqrs' : '7',
  'tuv'  : '8',
  'wxyz' : '9'}
  s=''
  for x in txt:
    if x.isalpha():
      A=[k for k in d if x.lower() in k]
      s+=d[A[0]]
    else:
      s+=x
  return s

