
def eratosthenes(num):
  return [n for n in range(2,num+1) if (n==2 or n>1 and n%2 and 
      all(n%i for i in range(3,int(n**.5)+1,2)))]

