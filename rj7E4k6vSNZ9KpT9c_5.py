
def factor_chain(lst):
  return all([lst[-1] % num == 0 for num in lst[:-1]]);

