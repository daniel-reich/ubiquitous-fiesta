
def sigilize(desire):
  import re
  string = re.sub("[aeiouAEIOU]|\s", "", desire)
  unique_string = ""
  for letter in string[::-1]:
    if letter not in unique_string:
      unique_string += letter
  return unique_string[::-1].upper()

