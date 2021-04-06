
def missing_letter(lst):
  return [chr(ord(x)+1) for x in lst if chr(ord(x)+1) not in lst][0]

