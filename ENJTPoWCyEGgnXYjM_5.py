
def percent_filled(box):
  space=(len(box)-2)*(len(box[0])-2)
  count=0
  for i in box:
    for n in i:
      if n!='#' and n!=' ':
        count+=1
  return str(int(count/space*100))+'%'

