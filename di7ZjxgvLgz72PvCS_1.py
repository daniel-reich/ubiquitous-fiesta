
def validate_swaps(lst, txt):
  return [len(txt)==len(j) and sum([1 for i in range(len(j))if j[i]==txt[i]])==len(txt)-2 for j in lst]

