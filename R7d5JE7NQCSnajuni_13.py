
def convert_to_number(dictionary):
  return {k:int(v) if v.isdigit() else v for k, v in dictionary.items()}

