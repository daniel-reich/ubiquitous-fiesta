
def return_end_of_number(num):
  numend={1:'-ST',2:'-ND',3:'-RD'}
  if int(str(num)[-2:])>3 and int(str(num)[-2:])<21:
    return str(num)+'-TH'
  elif int(str(num)[-1])<4:
    return str(num)+numend[int(str(num)[-1])]
  return str(num)+'-TH'

