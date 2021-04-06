
def sums_of_powers_of_two(n):
  lst = d_to_b(n)
  return [2**i for i in range(len(lst)) if lst[i]]
  
def d_to_b(n):
  ret = []
  while n>0:
    ret.append(n%2)
    n//=2
  return ret

