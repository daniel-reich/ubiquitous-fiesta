
def make_happy(txt):
  txt_list = list(txt)
  poss_chars = [":", ";", "x", "8", "X"]
  for i in range(1, len(txt_list)):
    if txt_list[i] == "(" and txt_list[i-1] in poss_chars:
      txt_list[i] = ")"
  return "".join(txt_list)

