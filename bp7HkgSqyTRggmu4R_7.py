
def reverse_title(txt):
  txt_lst = txt.lower().split(' ')
  return ' '.join([t[0] + t[1:].upper() for t in txt_lst])

