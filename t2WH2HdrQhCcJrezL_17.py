
def eda_bit(start, end):
  ans = []
  x=range(start, end+1)
  for n in x:
    if n % 3 == 0  and n%5 ==0:
      ans.append("EdaBit")
​
    elif n % 3 == 0:
      ans.append("Eda")
​
    elif n % 5 == 0:
      ans.append("Bit")
​
    else:
      ans.append(n)
​
  return ans

