
def find_and_remove(dct):
  return {k:parse(v) for k,v in dct.items()}
​
def parse(dct):
  return {k:int(v) for k,v in dct.items() if v.isnumeric()}

