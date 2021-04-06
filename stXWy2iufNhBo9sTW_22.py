
def valid_rondo(s):
​
  if len(s) <3:
    return False
  if s[0] == 'A' and s[-1] == 'A':
    rule1 = True
  else:
    rule1 = False
  
  rule3 = True
  alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split()
  
  sset = list(set(s))
  
  for item in sset:
    count = s.count(item)
    if count != 1 and item != 'A':
      rule3 = False
      break
  
  maxim = s[-2]
  end = 0
  
  for n in range(26):
    if alph[n] == maxim:
      end = n
      break
  
  should_be = []
  
  for n in range(end):
    should_be.append(alph[n])
  
  rule2 = True
  
  for l8r in should_be:
    if l8r not in s:
      rule2 = False
      break
  
  rules = [rule1, rule2, rule3]
  print(rules)
  if False in rules:
    return False
  return True

