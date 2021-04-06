
def column_chart(productA, productB, target):
  sumsum = [productA[i]+ productB[i] for i in range(len(productA))]
  rows = max(max(sumsum),(max(target)+10)) //10+ 1 
  lst=[['   ', '| ', 'Mo ', 'Tu ', 'We ', 'Th ', 'Fr ', 'Sa ', 'Su ', '|']]
  for i in range(1,rows):
    tmp=[str((i)*10) + ' | ']
    for j in range (len(target)):
      if productA[j]>= (i)*10:
        tmp.append('++ ')
      else:
        if productB[j]>= (i)*10-productA[j]:
          tmp.append('** ')
        else:
          if (i)*10 == target[j]+10:
            tmp.append('__ ')
          else:
            tmp.append('   ')
      if (j== len(target)-1):
        tmp.append('|')
    lst.append(tmp)
  outout=''
  for i in lst[::-1]:
    out=''
    for c in i:
      out+=str(c)
    if 'Su ' in i:
      outout+=out
    else:
      outout+=out+'\n'
  return outout

