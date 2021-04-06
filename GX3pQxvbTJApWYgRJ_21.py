
def is_kaprekar(n):
  n_sq = n**2
  m = str(n_sq)
  num_dig = len(m)
  if num_dig % 2 == 0:
    left = int(m[:int(num_dig/2)])
    right = int(m[int(num_dig/2):])
  elif num_dig != 1:
    left = int(m[:int((num_dig-1)/2)])
    right = int(m[int((num_dig-1)/2):])
  else: 
    left = 0
    right = n_sq
    
  if left + right == n:
    return True
  else:
    return False

