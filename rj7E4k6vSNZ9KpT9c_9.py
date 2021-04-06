
def factor_chain(lst):
  wrong = 0
  for i in range(1, len(lst)):
    if lst[i]%lst[i - 1] != 0:
      wrong += 1
  return(wrong == 0)

