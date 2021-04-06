
def convert_to_number(obj):
  for item in obj:
    obj[item] = int(obj[item])
  return obj

