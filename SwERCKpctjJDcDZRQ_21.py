
def longest_string(str1, str2):
  string = ""
  for x in str1:
    if x not in string:
      string += x
  for y in str2:
    if y not in string:
      string += y
  close = sorted(string)
  answer = ""
  for x in close:
    answer += x
  return answer

