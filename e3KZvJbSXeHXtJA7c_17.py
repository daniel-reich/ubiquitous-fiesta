
def sum_missing_numbers(lst):
  m,M = min(lst),max(lst)
  return (m+M)*(M-m+1)//2 - sum(lst)

