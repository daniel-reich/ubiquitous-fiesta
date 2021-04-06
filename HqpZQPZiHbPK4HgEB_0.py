
def maxmin(n):
  swaps, n = [n], str(n)
  for a in range(len(n)):
    for b in range(len(n)):
      if a != b:
        swap = list(n)
        swap[a], swap[b] = swap[b], swap[a]
        if swap[0] != '0':
          swaps.append(int(''.join(swap)))
  return (max(swaps), min(swaps))

