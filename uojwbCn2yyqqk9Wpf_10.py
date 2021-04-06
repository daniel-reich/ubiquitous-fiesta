
def is_untouchable(n):
  touch = [i for i in range(2,1+n**2) if div_sum(i)==n]
  return "Invalid Input" if n<2 else touch if touch else True
​
def div_sum(n):
    half = [i for i in range(1,1+int(n**.5)) if not n%i]
    return sum(half)+sum(n//i for i in half) - (n**.5)*(n**.5%1==0) -n

