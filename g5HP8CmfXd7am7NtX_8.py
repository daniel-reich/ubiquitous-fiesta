
def keyboard_mistakes(txt):
  l=[]
  i=0
​
  l=list(txt)
​
  for i in range(len(l)):
    if l[i] == '4' :
      l[i] = "A"
    elif l[i] == '5':
      l[i] = 'S'
    elif l[i] == '0':
      l[i] = 'O'
    elif l[i] == '1':
      l[i] = 'I'
  lts=''.join(map(str,l))
​
  return lts

