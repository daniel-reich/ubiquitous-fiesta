
def isbn13(string):
  string_sum = 0
​
  if len(string) == 10:
    string = string[::-1]
    for enu_num, num in enumerate(string):
      if num == "X":
        num = 10
      string_sum += (enu_num + 1) * int(num)
​
    if string_sum % 11 == 0:
      string = string[::-1]
      string = "978" + string
​
      for num in range(11):
        string_sum = 0
        string = string[:-1] + str(num)
        validate = [1,3,1,3,1,3,1,3,1,3,1,3,1]
        string_lst = [int(digit) for digit in string]
​
        for valid, str_num in zip(validate, string_lst):
          string_sum += valid * str_num
​
        if string_sum % 10 == 0:
          return string
​
    else:
      return "Invalid"
​
  elif len(string) == 13:
    validate = [1,3,1,3,1,3,1,3,1,3,1,3,1]
    string_lst = [int(digit) for digit in string]
​
    for valid, str_num in zip(validate, string_lst):
      string_sum += valid * str_num
​
    if string_sum % 10 == 0:
      return "Valid"
    else:
      return "Invalid"

