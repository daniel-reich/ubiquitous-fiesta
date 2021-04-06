
def secret(txt):
  txt = txt.replace(".", " ")
  txt = txt.split()
  
  txt_middle = " ".join(txt[1:])
  tag_start = "<" + txt[0] + " "
  tag_end = "></" + txt[0] + ">"  
  class_middle = "class=" + "'" + txt_middle + "'"
  
  return tag_start + class_middle  + tag_end

