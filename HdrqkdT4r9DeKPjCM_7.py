
def is_polygonal(n):
  if n == 1:
    return "0th of all"
  elif n < 4:
    return False
  
  r_k = list()
  temp = 2 * (n-1)
  for k in range (3, n):
    i = 1
    temp_2 = k * (i*i+i)
    while temp_2 <= temp:
      if temp == temp_2:
        r_k.append((i, k))
        break
      i += 1
      temp_2 = k * (i*i+i)
    
  ret = list()
  for i, k in r_k:
    if i >= 11 and i <= 13:
      ith = str(i) + "th "
    elif (i%10) == 1:
      ith = str(i) + "st "
    elif (i%10) == 2:
      ith = str(i) + "nd "
    elif (i%10) == 3:
      ith = str(i) + "rd "
    else:
      ith = str(i) + "th "
    ret.append(ith + str(k) + "-gonal number")
  return ret

