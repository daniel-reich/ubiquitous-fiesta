
def trouble(num1, num2):
  string1 = False
  string2 = False
  rep_num = 0
  count = 1
  for n in range(len(str(num1)) - 1):
    if str(num1)[n] == str(num1)[n+1]:
      count += 1
      print(count)
      if count == 3:
        rep_num = int(str(num1)[n])
        string1 = True
        count = 1
        break
  if str(num2).count(str(rep_num)) >= 2:
    string2 = True
  print(str(string1) + ", " + str(string2))
  if string1 and string2:
    return True
  else:
    return False

