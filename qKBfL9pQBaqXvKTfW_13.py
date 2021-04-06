
def sum_of_slices(lst):
  x=[0]
  [x.append(i-1) for i in range(len(lst)+1) if sum(lst[max(x):i])>=100]
  return [sum(lst[x[i]:x[i+1]]) for i in range(len(x)-1)]+lst[x[-1]:]

