
def is_vampire(n):
  def even_perms(perms):
    
    half = int(len(perms[0]) / 2)
    
    permutations = []
​
    for perm in perms:
      p1l = perm[:half]
      p2l = perm[half:]
​
      p1s = ''
      for n in p1l:
        p1s += str(n)
      p2s = ''
      for n in p2l:
        p2s += str(n)
​
      p1 = int(p1s)
      p2 = int(p2s)
​
      if len(list(str(p1))) != len(list(str(p2))):
        continue
​
      permutation_combo = [p1, p2]
​
      if permutation_combo not in permutations:
        permutations.append(permutation_combo)
​
    return permutations 
​
    return p1, p2
  def odd_perms(perms):
​
    half = int(len(perms[0]) / 2)
    half1 = half + 1
​
    biggest = True
    tr = []
​
    for perm in perms:
      
      n1l = perm[:half1]
      n2l = perm[half1:]
​
      n1s = ''
      for item in n1l:
        n1s += str(item)
      n2s = ''
      for item in n2l:
        n2s += str(item)
​
      n1 = int(n1s)
      n2 = int(n2s)
​
      if len(list(str(n1))) - 1 != len(list(str(n2))):
        return 'ERROR L232'
      else:
        tr.append([n1, n2])
      
      n1l = perm[:half]
      n2l = perm[half:]
​
      n1s = ''
      for item in n1l:
        n1s += str(item)
      n2s = ''
      for item in n2l:
        n2s += str(item)
​
      n1 = int(n1s)
      n2 = int(n2s)
​
      if len(list(str(n2))) - 1 != len(list(str(n1))):
        return 'ERROR L251'
      else:
        tr.append([n1, n2])
​
    return tr
  def multi_test(perms, n):
​
    answer = False
​
    for pair in perms:
​
      n1 = int(pair[0])
      n2 = int(pair[1])
​
      product = n1 * n2
​
      if product == n:
        answer = True
        break
    
    return answer
​
  import itertools as i
  l = list(str(n))
  nl = []
  for item in l:
    nl.append(int(item))
  l = nl
  del nl
​
  permutations = list(i.permutations(l))
​
  if n <= 99:
    return 'Normal Number'
  
  even = False
  if len(list(str(n))) % 2 == 0:
    even = True
  
  if even == True:
    perms = even_perms(permutations)
  else:
    perms = odd_perms(permutations)
​
  answer = multi_test(perms, n)
​
  if answer == False:
    return 'Normal Number'
  else:
    if even == True:
      return 'True Vampire'
    else:
      return 'Pseudovampire'

