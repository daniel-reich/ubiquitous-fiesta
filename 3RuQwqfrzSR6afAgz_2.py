
def rail_fence_cipher(message, rails):
  k=2*rails-2
  A=[]
  for i in range(rails):
    B=[]
    for j in range(len(message)):
      if j%k==i or j%k==k-i:
        B.append(message[j])
    A.append(B)
  res=[''.join(x) for x in A]
  return ''.join(res)

