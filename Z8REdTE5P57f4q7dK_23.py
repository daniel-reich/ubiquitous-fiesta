
def collatz(n):
  tally = []
  while n > 1:
    if n %2 == 0:
      n = n//2
      tally.append(n)
    elif n %2 != 0:
      n = (n * 3) + 1
      tally.append(n)
  return (len(tally)+1, max(tally))

