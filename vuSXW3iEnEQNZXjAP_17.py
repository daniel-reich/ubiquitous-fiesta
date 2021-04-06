
def create_square(length):
  if length == None or length <= 0:
    return ""
  elif length == 1:
    return "#"
  elif length == 2:
    return "##\n##"
  else:
    return "\n".join(["#"*length, "\n".join(["#" + " "*(length-2) + "#"  for i in range(length - 2)]), "#"*length])

