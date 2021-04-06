
import itertools
def is_vampire(n):
  if n < 99: return "Normal Number"
  if len(str(n)) % 2 == 0:
    for i in itertools.permutations(str(n)):
      if int(str("".join(i))[:len(str(n))//2]) * int(str("".join(i))[len(str(n))//2:]) == n:
        return "True Vampire"
  else:
    for i in itertools.permutations(str(n)):
      if int(str("".join(i))[:len(str(n))//2]) * int(str("".join(i))[len(str(n))//2:]) == n:
        return 'Pseudovampire'
      if int(str("".join(i))[:len(str(n))//2+1]) * int(str("".join(i))[len(str(n))//2+1:]) == n:
        return 'Pseudovampire'
      
  return "Normal Number"

