
def digital_decipher(eMessage, key):
  A=eMessage
  d,r=divmod(len(eMessage), len(str(key)))
  B=[int(x) for x in d*str(key)+str(key)[:r]]
  C=[A[i]-B[i] for i in range(len(A))]
  D=[chr(x+ord('a')-1) for x in C]
  return ''.join(D)

