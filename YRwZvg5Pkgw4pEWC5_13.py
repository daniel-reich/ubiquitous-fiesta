
def flick_switch(lst):
  val = True
  ret_list = list()
  for i in lst:
    if i == "flick":
      val  = not val
    ret_list.append(val)
  return ret_list

