
def missing_letter(lst):
  return ''.join([chr(ord(x) + 1) for x in lst if chr(ord(x) + 1) not in lst and x != lst[-1]])

