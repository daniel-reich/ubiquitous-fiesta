
def hacker_speak(txt):
  x=''
  for i in txt:
    if i.lower()=="a":
      x+='4'
    elif i.lower()=='e':
      x+='3'
    elif i.lower()=='i':
      x+='1'
    elif i.lower()=='o':
      x+='0'
    elif i.lower()=='s':
      x+='5'
    else:
      x+=str(i)
  return x

