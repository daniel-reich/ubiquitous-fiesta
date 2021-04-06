
def left_slide(row):
  b=[]
  while 0 in row:
    row.remove(0)
    b+=[0]
  row=row+b
  for i in range(1,len(row)):
    if row[i]==row[i-1] and row[i]!=0:
      row=row[:i-1]+[row[i]*2]+row[i+1:]+[0]
  return row

