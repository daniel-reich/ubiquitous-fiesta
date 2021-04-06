
def sorting_steps(lst):
  def swap(lst, swaps = []):
    if lst == sorted(lst):
      return swaps
    else:
      s = []
      for n in range(1, len(lst)):
        pi = lst[n-1]
        ci = lst[n]
        if ci < pi:
          spi = ci
          sci = pi
          lst[n-1] = spi
          lst[n] = sci
          swaps.append(tuple([n-1, n]))
          break
      return swap(lst,swaps)
  swaps = swap(lst)
  return swaps

