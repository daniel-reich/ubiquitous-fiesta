
def secret_password(msg):
​
  #Step 1:
​
  if len([l8r for l8r in msg if l8r in 'abcdefghijklmnopqrstuvwxyz']) == len(msg) == 9:
    s1 = True
  else:
    s1 = False
  
  if s1 == False:
    return ' '.join(['BANG!'] * 3)
  
  #Step 2:
​
  part1 = msg[:3]
  part2 = msg[3:6]
  part3 = msg[6:]
​
  #Step 3:
​
  a_to_n_converter = {'abcdefghijklmnopqrstuvwxyz'[n]: n+1 for n in range(26)}
​
  part1 = list(part1)
​
  part1[0] = str(a_to_n_converter[part1[0]])
  part1[2] = str(a_to_n_converter[part1[2]])
​
  part1 = ''.join(part1)
​
  #Step 4:
​
  part2 = ''.join(list(reversed(part2)))
​
  #Step 5:
​
  alph = 'abcdefghijklmnopqrstuvwxyz'
  p3 = ''
​
  for l8r in part3:
    t = alph.index(l8r) + 1
​
    while t >= 26:
      print('l', t)
      t -= 26
    
    p3 += alph[t]
  
  part3 = p3
​
  del p3
  
  #Step 6:
​
  return part2 + part3 + part1

