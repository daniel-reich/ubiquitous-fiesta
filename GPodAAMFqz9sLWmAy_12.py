
def one_odd_one_even(n):
  new_num = str(n)
  if int(new_num[0]) % 2 == 0 and int(new_num[1]) % 2 != 0:
    return True
  elif int(new_num[0]) % 2 != 0 and int(new_num[1]) % 2 == 0:
    return True
  else:
    return False

