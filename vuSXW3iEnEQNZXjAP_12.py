
def create_square(le):
  if not le :
    le = -1
    return ''
  if le < 1 :
    return ''
  if le == 1:
    return "#"
  f,l = "#"*le+"\n","#"*le
  m = "#"+" "*(le-2)+"#\n"
  return (f+(m*(le-2))+l)

