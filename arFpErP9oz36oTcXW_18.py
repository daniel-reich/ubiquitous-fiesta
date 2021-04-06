
def secret(txt):
  txt_split = txt.split(".")
  tag = txt_split[0]
  classes = ""
  for i in range(1,len(txt_split)):
    classes += txt_split[i]
    if i != len(txt_split) - 1:
      classes += " "
  
  return("<{} class='{}'></{}>".format(tag, classes, tag))

