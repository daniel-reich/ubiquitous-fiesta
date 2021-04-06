
def sort_by_last(txt):
  l = txt.split(' ')
  
  def takeLast(elem):
    return elem[-1:]
  
  l.sort(key=takeLast)
  
  return " ".join(l)

