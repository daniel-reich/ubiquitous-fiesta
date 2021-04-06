
from itertools import permutations
def is_vampire(n):
  if n > 99:
    num = str(n); v = len(num)//2
    lst = [''.join(i) for i in permutations(list(num),len(num)) if i[0] != '0']
    if len(num)%2:
      if n in (int(i[:v+j])*int(i[v+j:]) for j in range(2) for i in lst):
        return 'Pseudovampire'
    else:
      if n in (int(i[:v])*int(i[v:]) for i in lst):
        return 'True Vampire'
  return 'Normal Number'

