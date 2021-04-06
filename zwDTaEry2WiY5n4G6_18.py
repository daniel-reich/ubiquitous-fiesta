
def digital_vowel_ban(n, ban):
  numbers = {'1':"one", '2':"two", '3':"three", '4':"four", '5':"five",
  '6':"six", '7':"seven", '8':"eight", '9':"nine", '0':"zero"}
  temp = ''
  for i in str(n):
    if ban not in numbers[i]:
      temp += i
  if len(temp) == 0:
    return "Banned Number"
  return int(temp)

