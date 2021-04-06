
def variable_valid(var):
  for i in range(len(var)):
    if i == 0:
      if not var[0].isalpha():
        return False
    if var[i] == " ":
      return False
        
  return True

