
def magic(txt):
  lst = txt.split()
  day_month = int(lst[0]) * int(lst[1])
  last_1 = int(lst[2][-1])
  last_2 = int(lst[2][2:])
  last_3 = int(lst[2][3:])
  if day_month == (last_1 or last_2 or last_3):
    return True
  else:
    return False

