
def format_phone_number(lst):
  lst.insert(6,"-")
  lst.insert(3," ")
  lst.insert(3,")")
  lst.insert(0,"(")
  return "".join(map(str,lst))

