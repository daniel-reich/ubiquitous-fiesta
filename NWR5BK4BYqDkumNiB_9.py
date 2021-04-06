
def digital_division(n):
  s_n = str(n)
  correct_count = 0
  if all([n%int(s)==0 for s in s_n if int(s)!=0]):
    correct_count +=1
  if n % sum([int(s) for s in s_n]) == 0:
    correct_count += 1
    
  product=1
  for s in s_n:
   product *= int(s) 
  if product != 0 and n % product == 0:
    correct_count += 1
  
  if correct_count == 3:
    return "Perfect"
  elif correct_count == 0:
    return "Indivisible"
  else:
    return correct_count

