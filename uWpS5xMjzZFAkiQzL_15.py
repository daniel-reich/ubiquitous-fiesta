
def odds_vs_evens(num):
  odd = []
  even = []
  lst = [int(number) for number in str(num)]
  for i in lst:
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  return "even" if sum(odd) < sum(even) else "odd" if sum(odd) > sum(even) else "equal"

