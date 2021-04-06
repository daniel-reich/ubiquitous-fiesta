
def remix(txt, lst):
  zip_t_l = list(zip(lst,txt))
  s_zip = sorted(zip_t_l, key=lambda x: x[0])
  return("".join([x[1] for x in s_zip]))

