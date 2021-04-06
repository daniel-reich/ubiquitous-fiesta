
def replace_the(txt):
  A=txt.split()
  for i in range(len(A)):
    if A[i]=='the':
      if A[i+1][0] in 'aeiou':
        A[i]='an'
      else:
        A[i]='a'
  return ' '.join(A)

