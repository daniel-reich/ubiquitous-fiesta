
def left_slide(row):
  i,l=0,len(row)
  while 0 in row: row.remove(0)
  while i<len(row)-1:
    if row[i]==row[i+1]:
      row[i]=2*row[i]
      del row[i+1]
    i+=1
  return (row+l*[0])[:l]

