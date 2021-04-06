
def max_collatz(num):
  lst = [num]
  while num!=1:   
    if num%2:
      num = (num*3)+1     
    else:     
      num//=2
    lst.append(num)
  return max(lst)

