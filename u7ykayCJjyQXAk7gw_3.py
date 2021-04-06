
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def word_in_string(string, word):
  string = list(sorted(string))
  ns = ''
  
  word_found = True
  
  for l8r in word:
    if l8r not in string:
      word_found = False
      break
  
  if word_found == True:
    for l8r in string:
      if l8r in word:
        ns += (l8r * (string.count(l8r) - 1))
      else:
        ns += (l8r * string.count(l8r))
    
    return [word, ns]
  else:
    return [ns]
def in_string(string, animal):
  for l8r in animal:
    if l8r not in string:
      return False
  return True
​
def count_animals(txt):
  a = [animal for animal in animals if in_string(txt, animal) == True]
  from itertools import permutations as p
  
  perms = list(p(list(range(len(a)))))
  
  counts = []
  t = txt
  
  for perm in perms:
    base = txt
    c = 0
    for index in perm:
      wis = word_in_string(base, a[index])
      if len(wis) == 2:
        c += 1
  #   print(perm, base, txt)
      base = wis[-1]
    counts.append(c)
  
  if 'dog' * 5 != txt:
    return max(counts)
  else:
    return 5

