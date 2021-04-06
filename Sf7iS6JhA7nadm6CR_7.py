
def divisibility_rule(n):
  seq = [1, 10, 9, 12, 3, 4]
  A=[]
  while n not in A:
    A.append(n)
    B=[int(x) for x in str(n)][::-1]
    n=sum(B[i]*seq[i%6] for i in range(len(B)))
  return A[-1]

