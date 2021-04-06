
def odds_vs_evens(num):
  num = str(num)
  odd, even = [] , []
  for n in num:
    if int(n)%2==0:
      even.append(int(n))
    else:
      odd.append(int(n))
  return "odd" if sum(odd)>sum(even) else "even" if sum(even)>sum(odd) else "equal"

