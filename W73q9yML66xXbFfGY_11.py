
def coloured_triangle(row):
  while len(row)>1:
    temp=''
    for i in range(1,len(row)):
      if row[i]==row[i-1]:
        temp+=row[i]
      else:
        temp+=[j for j in 'RGB' if j not in row[i]+row[i-1]][0]
    row=temp
  return row

