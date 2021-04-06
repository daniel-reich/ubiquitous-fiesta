
def get_frame(w, h, ch):
  if w<=2 or h<=2:
    return 'invalid'
  lst=[]
  for i in range(h):
    lst.append([])
    if i==0 or i==h-1:
      lst[i].append(ch*w)
    else:
      lst[i].append(ch+' '*(w-2)+ch)
  return lst

