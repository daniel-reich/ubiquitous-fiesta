
def letters_only(x):
  return False if not x else all([bool(i) if i.isalpha() and i.islower() or i == ' ' else False for i in x ])

