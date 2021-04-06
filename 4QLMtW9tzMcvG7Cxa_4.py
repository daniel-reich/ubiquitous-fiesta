
def resistance_calculator(lst):
  return [round(1/sum([1/r for r in lst]),2),round(sum(lst),1)] if 0 not in lst else [0,sum(lst)]

