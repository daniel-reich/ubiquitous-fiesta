
def bird_code(lst):
  codes = []
  for i in lst:
    i = i.replace('-', ' ').upper().split()
    if len(i)==1:
      codes.append(i[0][:4])
    elif len(i)==2:
      codes.append(i[0][:2] + i[1][:2])
    elif len(i)==3:
      codes.append(i[0][0]+i[1][0]+i[2][:2])
    else:
      codes.append(i[0][0]+i[1][0]+i[2][0]+i[3][0])
  return codes

