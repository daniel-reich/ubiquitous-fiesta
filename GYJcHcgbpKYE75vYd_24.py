
def return_end_of_number(num):
  if (num%100)//10==1 or num%10 not in [1,2,3]:
    return str(num)+'-TH'
  elif num%10 == 1:
    return str(num)+'-ST'
  elif num%10 == 2:
    return str(num)+'-ND'
  else:
    return str(num)+'-RD'

