
def maya_number(n):
  if n == 0:
    lst = [0]
  else:
    lst = []
  while n > 0:
    lst.append(n % 20)
    n = n // 20
  lst = lst[::-1]
  maya = {0:'@',1:'o',2:'oo',3:'ooo',4:'oooo',5:'-',6:'o-',7:'oo-',8:'ooo-',9:'oooo-',10:'--',11:'o--',12:'oo--',13:'ooo--',14:'oooo--',15:'---',16:'o---',17:'oo---',18:'ooo---',19:'oooo---'}
  return [maya[i] for i in lst]

