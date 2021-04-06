
def portion_happy(n):
  first = n[0] == n[1]
  last = n[-1] == n[-2]
  others = sum(n[i] == n[i-1] or n[i] == n[i+1] for i in range(1, len(n)-1))
  return (first + last + others) / len(n)

