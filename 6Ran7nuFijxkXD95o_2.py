
def keyboard_shortcut(txt):
  txt = txt.replace('Ctrl + C','0').replace('Ctrl + V','1')
  print (txt)
  txt = list(txt.split(' '))
  ans = []
  txt_c = []
  for i in txt:
    if i=='0': txt_c=ans
    elif i=='1': ans=ans+txt_c
    else: ans.append(i)
  return ' '.join(ans)

