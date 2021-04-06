
def is_untouchable(n):
  a = [i for i in range(2,n**2+1) if (1 + sum(sum({j,i//j}) for j in range(2,int(i**0.5)+1) if not i%j)) == n]
  return "Invalid Input" if n<2 else a if a else True

