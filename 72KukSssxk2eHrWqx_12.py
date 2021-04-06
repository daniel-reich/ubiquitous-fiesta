
def char_at_pos(r, s):
  def is_even(n):
    return n%2==0
  
  tr = []
  
  if s == 'even':
    for n in range(len(r)): 
      if is_even(n) == True and is_even(len(r)) == True:
        tr.append(r[n])
      if is_even(n) == False and is_even(len(r)) == False:
        tr.append(r[n])
  else:
    for n in range(len(r)):
      if is_even(n) == False and is_even(len(r)) == True:
        tr.append(r[n])
      if is_even(n) == True and is_even(len(r)) == False:
        tr.append(r[n])
  
  if isinstance(r, list) == True:
    return tr
  else:
    return ''.join(tr)

