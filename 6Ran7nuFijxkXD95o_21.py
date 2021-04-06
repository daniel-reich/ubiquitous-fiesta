
def keyboard_shortcut(txt):
  txt=txt.replace('Ctrl + ', '')
  A=txt.split()
  R=[]
  S=[]
  for x in A:
    if x not in 'CV':
      R.append(x)
    else:
      if x=='C':
        S.append(x)
      else:
        if S:
          R.append(' '.join(R))
          S.pop()
  return ' '.join(R)

