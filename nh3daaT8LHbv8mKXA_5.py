
def text_to_num(phone):
  table = phone.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', '22233344455566677778889999')
  return phone.translate(table)

