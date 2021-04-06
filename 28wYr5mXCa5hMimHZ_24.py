
def valid_name(name):
  lname = name.split(" ")
  
  if len(lname) == 2:
    if check_initial(lname[0]) and check_word(lname[1]):
      return True
    else:
      return False
  elif len(lname) == 3:
    if (check_initial(lname[0]) or check_word(lname[0])) and (check_initial(lname[1]) or (check_word(lname[1]) and not check_initial(lname[0]))) and (check_word(lname[2])):
      return True
    else:
      return False
  else:
    return False
    
def check_initial(string):
  if len(string) != 2:
    return False
  if not (65 <=ord(string[0]) and ord(string[0]) <= 90):
    return False
  if string[-1] != '.':
    return False
​
  return True
  
def check_word(string):
  if not len(string) > 2:
    return False
  if not (65 <=ord(string[0]) and ord(string[0]) <= 90):
    return False
  if '.' in string:
    return False
​
  return True

