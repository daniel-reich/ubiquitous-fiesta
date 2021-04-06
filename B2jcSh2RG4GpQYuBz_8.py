
def is_valid_phone_number(txt):
  par1 = txt.find('(')
  par2 = txt.find(')')
  dash = txt.find('-')
  space = txt.find(' ')
  if(par1 == 0 and par2 == 4 and dash == 9 and space == 5 and len(txt) == 14):
      return True
  return False

