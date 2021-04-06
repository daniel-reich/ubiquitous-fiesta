
def is_prime (n):
  if n == 1 or n == 0 :
    return False
  for i in range (2,n):
    if n%i == 0:
      return False
  return True
​
​
​
​
def extract_primes (num):
  num_list = list (str(num))
  num_list.reverse()
  prime_list = [ ]
  for len_num in range (1,len (num_list)+1):
​
    for i in range (len(num_list)-len_num + 1 ):
      c = 0 
      decimal_num = 0 
      while c!= (len_num ):
        decimal_num += (int (num_list[i+c]))*10**c
        mem = num_list[i+c]
        c+=1 
        
​
      if is_prime (decimal_num) and int (mem) != 0:
        prime_list.append (decimal_num)
  prime_list.sort()
  return prime_list

