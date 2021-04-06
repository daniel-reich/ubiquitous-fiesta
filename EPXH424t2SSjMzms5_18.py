
def remix(txt, lst):
  txt_list = [i for i in txt]
  new_dict = dict(zip(lst, txt_list))
  return ''.join(list(new_dict.values()))

