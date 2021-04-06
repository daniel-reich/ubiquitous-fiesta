
def to_snake_case(txt):
  new_lst = []
  for i in range(0, len(txt)):
    if txt[i].upper() == txt[i]:
      new_lst.append('_' + txt[i].lower())
    else:
      new_lst.append(txt[i])
  return ''.join(new_lst)
​
def to_camel_case(txt):
  new_lst = []
  str_split = txt.split('_')
  for i in range(0, len(str_split)):
    if i > 0:
      new_lst.append(str_split[i].capitalize())
    else:
      new_lst.append(str_split[i])
  return ''.join(new_lst)

