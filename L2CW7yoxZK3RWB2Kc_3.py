
def nico_cipher(message, key):
  message=message+'*'*(len(key)-len(message)%len(key))
  A=[]
  for i in range(len(key)):
     A.append((key[i],[message[j] for j in range(len(message)) if j%len(key)==i]))
  A=sorted(A, key=lambda x: (x[0], A.index(x)))
  B=[x[1] for x in A]
  C=[''.join(x) for x in zip(*B)]
  return ''.join(C).replace('*', ' ')

