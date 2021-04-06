
def arrow(num):
  txt_ar = []
  txt = ">"
  txt_ar.append(txt)
  for line in range(num-1):
    txt = ">" + txt
    txt_ar.append(txt)
    
  if num % 2 == 0:
    txt_ar.append(txt)
    
  for line in range(1, num):
    txt = ">" * (num - line)
    txt_ar.append(txt)
    
  return txt_ar

