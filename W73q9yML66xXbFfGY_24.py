
def coloured_triangle(row):
  while len(row)>1:
    trow=""
    for x,y in zip(row,row[1:]):
      d=list(set("RGB")-set([x,y]))
      if len(d)==2:
        trow+=x
      else:
        trow+=d[0]
    row=trow
  return row

