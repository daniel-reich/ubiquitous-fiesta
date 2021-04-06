
def remix(txt, lst):
  new_txt = ''.join([value for value in  dict(zip(lst, txt)).values()])
  return new_txt

