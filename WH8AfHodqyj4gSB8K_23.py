
def is_authentic_skewer(s):
  H=None;E=False;D='-';C='AEIOU'
  if s[0]in C or s[0]==D:return E
  if s[-1]in C or s[-1]==D:return E
  G=0;F=0
  for A in s[1:]:
    if A==D:G+=1
    else:break
  for A in s[1:]:
    if F>G:return E
    elif A!=D:
      if F!=G:return E
      F=0
    elif A==D:F+=1
  B=H
  for A in s:
    if A in C and B==0:return E
    elif A not in C and A!=D and B==1:return E
    elif A in C and(B==1 or B==H):B=0
    elif A not in C and A!=D and(B==0 or B==H):B=1
  return True

