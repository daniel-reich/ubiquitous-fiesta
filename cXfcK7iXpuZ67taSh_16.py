
def mystery_func(txt):
  num=[]
  zimu=[]
  txt1=''
  for i in txt:
    if i in 'ABCDEFHIJKLMNOPQRSTUVWXYZ':
      zimu+=i
    else:
      num+=i
  for j in range (0,len(num)):
    txt1=txt1+zimu[j]*int(num[j])
  return txt1

