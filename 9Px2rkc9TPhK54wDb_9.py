
def ecg_seq_index(n):
  def gcd(a,b):
    while a>0:
      a,b = b%a,a
    return b
  
  lst = [1,2]
  while True:
    new = 2
    while new in lst or gcd(new,lst[-1])==1:
      new+=1
    lst+=[new]
    if new == n:
      return len(lst)-1

