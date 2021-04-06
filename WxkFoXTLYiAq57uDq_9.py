
def find_and_remove(dct):
  return {k1: {k2: int(v2) for k2, v2 in dct[k1].items()if v2.isnumeric()} for k1 in dct}

