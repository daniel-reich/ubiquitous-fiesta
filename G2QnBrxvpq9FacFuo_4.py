
def possible_path(lst):
  
  valid_pair = lambda n1, n2: True if n1 == 'H' and n2 in range(1, 5) or n2 == 'H' and n1 in range(1, 5) else False
  answer = True
  
  for n in range(len(lst) - 1):
    ci = lst[n]
    ni = lst[n+1]
    
    answer = valid_pair(ci, ni)
    
    if answer == False:
      break
  
  return answer

