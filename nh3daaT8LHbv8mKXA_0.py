
def text_to_num(phone):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  num = "22233344455566677778889999"
  dic = dict(zip(alpha,num))
  return "".join([dic[i] if i.isalpha() else i for i in phone])

