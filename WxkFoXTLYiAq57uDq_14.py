
def find_and_remove(dct):
  return {key: {k: int(v) for k, v in val.items() if v.isdigit()} for key, val in dct.items()}

