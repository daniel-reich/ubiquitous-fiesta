
def is_polygonal(n):
  out=[]
  for i in range (3,70000):
    summ=1
    for j in range (1,70000):
      summ+=i*j
      if(summ == n):
        if (int(str(j)[-1])==1 and j!=11):
          suff='st'
        elif (int(str(j)[-1])==2 and j!=12):
          suff='nd'
        elif (int(str(j)[-1])==3 and j!=13):
          suff='rd'
        else:
          suff='th'
        out.append(str(j)+suff + ' ' + str(i) + '-gonal number')
      elif (summ > n):
        break
  return out if n>=4 else "0th of all" if (n<2) else False

