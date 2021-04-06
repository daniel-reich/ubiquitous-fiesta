
def special_reverse_string(txt):
  list_str = list(txt)
  list_str.reverse()
  list_str = list(filter( lambda x: x!=" ", list_str))
  print(list_str)
  reverse = []
  for char in txt:
    if char == " ":
      reverse.append(" ")
    elif char.isupper():
      reverse.append(list_str.pop(0).upper())
    else:
      reverse.append(list_str.pop(0).lower())
  string =""
  return string.join(reverse)

