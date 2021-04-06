
def next_prime(num):
  lst = [ ]  
  for n in range(1,200):
    for i in range(2,n//2+1):
      if n%i == 0:break
    else: lst.append(n)
  for i in lst:
    if num in lst: return num
    if i >num:return i

