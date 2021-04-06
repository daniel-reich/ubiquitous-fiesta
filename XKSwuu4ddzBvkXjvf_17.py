
import re
def is_prime(n):
  return divmod(2**(n-1), n)[1]==1
def sum_ord(x):
  if x.isalpha():
    return sum(ord(y)-ord('a')+1 for y in x)
  elif x.isdigit():
    return sum(int(y) for y in x)
def sentence_primeness(sentence):
  A=[x for x in re.findall('[\w]+', sentence)]
  B=[sum_ord(x.lower() if x.isalpha else x) for x in A]
  if is_prime(sum(B)):
    return "Prime Sentence"
  else:
    K=[]
    for i in range(len(B)):
      if is_prime(sum(B)-B[i]):
        K.append(i)
    if K:
      return "Almost Prime Sentence ({})".format(A[K[0]])
    else:
      return "Composite Sentence"

