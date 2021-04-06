
def word_to_decimal(word):
  alpha='abcdefghijklmnopqrstuvwxyz'
  A=[alpha.index(x) for x in word.lower()]
  n=max(A)+11
  B=[x+10 for x in A]
  C=[B[i]*n**(len(B)-i-1) for i in range(len(B))]
  return sum(C)

