
def convert_to_number(dictionary):
  for key in dictionary.keys():
    dictionary[key] = int(dictionary[key])
  return dictionary

