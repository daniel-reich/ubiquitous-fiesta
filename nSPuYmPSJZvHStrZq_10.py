
def oddeven(lst):
  odd_cnt = 0
  even_cnt = 0
  
  for num in lst:
    if num % 2 != 0:
      odd_cnt += 1
    else:
      even_cnt += 1
      
  if odd_cnt > even_cnt:
    return True
  else:
    return False

