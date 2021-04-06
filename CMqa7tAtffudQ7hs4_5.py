
def sorting_steps(lst):
    lst = lst[:]
    swaps = []
    for _ in range(len(lst)):
      for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
          lst[i], lst[i+1] = lst[i + 1], lst[i]
          swaps.append((i, i+1))
    return swaps

