
def text_to_num(phone):
  import re
  s = re.sub(r"(A|B|C)", "2",phone)
  s = re.sub(r"(D|E|F)", "3",s)
  s = re.sub(r"(G|H|I)", "4",s)
  s = re.sub(r"(J|K|L)", "5",s)
  s = re.sub(r"(M|N|O)", "6",s)
  s = re.sub(r"(P|Q|R|S)", "7",s)
  s = re.sub(r"(T|U|V)", "8",s)
  s = re.sub(r"(W|X|Y|Z)", "9",s)
  return s

