
def digits_count(num):
  result = 0
  print(num)
  if num > 9 or num< -9:
    return help(result + 1, num / 10)
  else:
    return help(result, num/10)
​
​
​
def help(result, num):
  if num < 10 and num > -10:
    return result + 1
  else:
    return help(result + 1, num / 10)

