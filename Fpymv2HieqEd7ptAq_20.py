
def split(txt):
  lst = []
  bracket_number = 0
  bracket_member = ''
  for i in txt:
    if i == "(":
      bracket_number += 1
      bracket_member += i
    if i == ")":
      bracket_number -= 1
      bracket_member += i
      if bracket_number == 0:
        lst.append(bracket_member)
        bracket_number = 0
        bracket_member = ''
  return lst

