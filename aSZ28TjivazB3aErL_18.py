
def letters_only(s):
  return not s=="" and all([(i.isalpha() and i.islower()) or i==" "  for i in s])

