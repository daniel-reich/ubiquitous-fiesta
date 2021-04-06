
def text_to_num(phone):
  intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  outtab = "22233344455566677778889999"
  trantab = str.maketrans(intab, outtab)
​
  return phone.translate(trantab)

