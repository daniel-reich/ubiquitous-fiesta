
def collatz(n):
  lst, x = [n], 0
  while lst[-1] != 1:
    lst.append(lst[-1] * 3 + 1 if lst[-1] % 2 else lst[-1] / 2); x += 1
  return [x, max(lst)]

