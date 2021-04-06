
def letters_only(s):
  return all([s.replace(" ", "").isalpha(), s.islower()])

