
def can_build(txt1, txt2):
  txt1_lst = txt1.split()
  txt2_lst = txt2.split()
  txt1 = "".join(txt1_lst)
  txt2 = "".join(txt2_lst)
  count = 0
  for char in range(len(txt1)):
    if txt1[char] in txt2:
      count += 1
      txt2 = txt2.replace(txt1[char], "", 1)
  if count == len(txt1):
    return True
  else:
    return False

