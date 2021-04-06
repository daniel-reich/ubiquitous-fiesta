
def create_square(length):
  try:
    if length <= 0:
      return ""
    elif length == 1:
      return "#"
    else:
      return "#"*length+"\n"+(length-2) * str("#"+" "*(length-2)+"#"+"\n")+ "#"*length
  except:
    return ""

