
def how_many_missing(lst):
  return 0 if lst==[] else len(range(min(lst),max(lst)+1))-len(lst)

