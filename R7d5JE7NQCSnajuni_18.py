
def convert_to_number(dictionary):
  return {
    key: int(value) 
    for key, value in dictionary.items()
  }

