
def prime_factorize(num):
 print(num)
 new = []
 if num <= 1:
  return []
 else:
  for i in range(2,num+1):
   while True:
    if num%i == 0:
     new.append(i)
     num = num//i
    else:
     break
 return new

