
def how_mega_is_it(n):
  n = str(n)
  
  if len(n) < 3:
    return 'not a mega milestone'
  else:
    if '.' in n:
      n = n.split('.')[0]
    if '-' in n:
      n = n.replace('-', '')
    d = len(n) - 3
    tr = []
    if d > 0:
      
      for num in range(d):
        tr.append('MEGA')
    
    tr.append('MEGA')
    tr.append('milestone')
    
    return ' '.join(tr)

