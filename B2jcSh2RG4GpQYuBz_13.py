
def is_valid_phone_number(txt):
  new=txt.split(") ")
  return new[0][0]=="(" and len(new[0])==4 and new[1][3]=="-" and len(new[1])==8

