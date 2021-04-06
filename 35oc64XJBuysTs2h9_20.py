
def get_quartiles(lst, method):
  def Turkey(lst):
​
    q0 = min(lst)
    q4 = max(lst)
​
    lst = sorted(lst)
​
    if len(lst) % 2 == 0:
      
      n1index = int(len(lst)/2) - 1
      n2index = n1index + 1
​
      n1 = lst[n1index]
      n2 = lst[n2index]
​
      q2 = (n1 + n2) / 2
​
      lower = lst[:n2index]
      upper = lst[n2index:]
    else:
      
      mindex = int(len(lst) / 2) 
​
      q2 = lst[mindex]
      
      lower = list(lst[:mindex])
      lower.append(lst[mindex])
      upper = lst[mindex:]
​
    
    if len(lower) % 2 == 0:
      
      n1index = int(len(lower) / 2) - 1
      n2index = n1index + 1
​
      n1 = lower[n1index]
      n2 = lower[n2index]
​
      q1 = (n1 + n2) / 2
    else:
​
      mindex = int(len(lower) / 2)
​
      q1 = lower[mindex]
    
    if len(upper) % 2 == 0:
      
      n1index = int(len(upper) / 2) - 1
      n2index = n1index + 1
​
      n1 = upper[n1index]
      n2 = upper[n2index]
​
      q3 = (n1 + n2) / 2
    else:
​
      mindex = int(len(upper) / 2)
​
      q3 = upper[mindex]
    
    return [q0, q1, q2, q3, q4]
  def Moore_McCab(lst):
​
​
    q0 = min(lst)
    q4 = max(lst)
​
    lst = sorted(lst)
​
    if len(lst) % 2 == 0:
      
      n1index = int(len(lst)/2) - 1
      n2index = n1index + 1
​
      n1 = lst[n1index]
      n2 = lst[n2index]
​
      q2 = (n1 + n2) / 2
​
      lower = lst[:n2index]
      upper = lst[n2index:]
    else:
      
      mindex = int(len(lst) / 2) 
​
      q2 = lst[mindex]
      
      lower = list(lst[:mindex])
      upper = lst[mindex + 1:]
​
    
    if len(lower) % 2 == 0:
      
      n1index = int(len(lower) / 2) - 1
      n2index = n1index + 1
​
      n1 = lower[n1index]
      n2 = lower[n2index]
​
      q1 = (n1 + n2) / 2
    else:
​
      mindex = int(len(lower) / 2)
​
      q1 = lower[mindex]
    
    if len(upper) % 2 == 0:
      
      n1index = int(len(upper) / 2) - 1
      n2index = n1index + 1
​
      n1 = upper[n1index]
      n2 = upper[n2index]
​
      q3 = (n1 + n2) / 2
    else:
​
      mindex = int(len(upper) / 2)
​
      q3 = upper[mindex]
    
    return [q0, q1, q2, q3, q4]
  def Mendenhall_Sincich(lst):
​
    q0 = min(lst)
    q4 = max(lst)
​
    lst = sorted(lst)
​
    q1ri = (len(lst) + 1) / 4
​
    if q1ri - int(q1ri) >= .5:
      q1i = int(q1ri) + 1
    else:
      q1i = int(q1ri)
    
    q1 = lst[q1i - 1]
​
    if len(lst) % 2 == 0:
      
      n1index = int(len(lst)/2) - 1
      n2index = n1index + 1
​
      n1 = lst[n1index]
      n2 = lst[n2index]
​
      q2 = (n1 + n2) / 2
    else:
      
      mindex = int(len(lst) / 2) 
​
      q2 = lst[mindex]
    
    q3ri = 3 * q1ri
    if q3ri - int(q3ri) > .5:
      q3i = int(q3ri) + 1
    else:
      q3i = int(q3ri)
​
    q3 = lst[q3i - 1]
​
    return [q0, q1, q2, q3, q4]
​
  if method == 'T':
    return Turkey(lst)
  elif method == 'MM':
    return Moore_McCab(lst)
  elif method == 'MS':
    return Mendenhall_Sincich(lst)
  else:
    return 'Incorrect Method: {}'.format(method)

