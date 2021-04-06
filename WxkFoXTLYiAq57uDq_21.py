
def find_and_remove(dct):
  return {kk:{k:int(v) for k,v in vv.items() 
    if v.isnumeric()} for kk,vv in dct.items()}

