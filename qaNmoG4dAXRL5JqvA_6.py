
def sum_fractions(lst):
  return round(sum(lst[i][0]/lst[i][1] for i in range(len(lst))))

