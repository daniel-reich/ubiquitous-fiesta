
def print_all_groups():
  new_string = ""
  forms = "abcde"
  for i in range(1, 7):
    for form in forms:
      new_string = new_string + str(i) + form + ", "
      
  return new_string[:-2]

