
def numbers_need_friends_too(n):
  
  new_n = ''
  prev_indexes = []
  
  for index in range(len(str(n))):
    if index in prev_indexes:
      continue
    digit = str(n)[index]
    try:
      next_digit = str(n)[index + 1]
    except IndexError:
      next_digit = ''
  # print(digit, next_digit)
    if next_digit != digit:
      new_n += digit * 3
    else:
      new_n += digit
      ni = index + 1
      try:
        while str(n)[ni] == digit:
          prev_indexes.append(ni)
          ni += 1
          new_n += digit
      except IndexError:
        continue
  
  return int(new_n)

