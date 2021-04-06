
def forbidden_letter(char, lst):
  f_l = [c for c in lst if char in c]
  if len(f_l) >= 1:
    return False
  else:
    return True

