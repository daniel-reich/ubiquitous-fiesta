
def collatz(n):
  lst = [n]
  while n > 1:
    if n % 2 == 0:
      n /= 2
      lst.append(n)
    else:
      n = n *3 +1
      lst.append(n)
  return (len(lst), max(lst))

