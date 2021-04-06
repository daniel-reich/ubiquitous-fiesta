
def monkey_talk(text):
  args=text.split()
  transl=""
  for i in args:
    if i[0] in ["A","a","E","e","I","i","O","o","U","u"]:
      transl+="Eek "
    else:
      transl+="Ook "
  return(transl[0]+transl[1:len(transl)-1].lower()+".")

