
def longest_run(lst):
  return max([abs(lst[i] - lst[j]) + 1 for i in range(1, len(lst)) for j in range(i + 1)
           if abs(lst[i] - lst[j]) == len(lst[j: i + 1]) - 1])

